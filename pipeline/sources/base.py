"""Base class for all TCKC pipeline source connectors."""
import logging
from abc import ABC, abstractmethod

logger = logging.getLogger('tckc_pipeline')


class BaseSourceConnector(ABC):
    """Abstract base for API source connectors.

    Subclasses must implement:
      - source_name: str property
      - category: str property (default tracker category for results)
      - _fetch_page(...): fetch one page/batch of results from the API
      - _parse_result(raw): convert a single API result to a normalized dict
    """

    @property
    @abstractmethod
    def source_name(self) -> str:
        """Short identifier for this source (e.g. 'congress_gov')."""
        ...

    @property
    @abstractmethod
    def category(self) -> str:
        """Default tracker category for entries from this source."""
        ...

    @abstractmethod
    def _fetch_page(self, since_date, **kwargs):
        """Fetch one page of results from the API.
        Returns (raw_results_list, has_more_pages)."""
        ...

    @abstractmethod
    def _parse_result(self, raw) -> dict:
        """Convert a single raw API result to a normalized dict."""
        ...

    def fetch_since(self, since_date, rate_limiter=None):
        """Fetch all results since the given date, handling pagination."""
        results = []
        seen_ids = set()
        kwargs = {'page': 1}

        while True:
            if rate_limiter:
                rate_limiter.wait_if_needed(self.source_name)

            try:
                raw_results, has_more = self._fetch_page(since_date, **kwargs)
            except Exception as e:
                logger.warning(f'{self.source_name}: fetch failed at page {kwargs.get("page", "?")}: {e}')
                break

            if not raw_results:
                break

            for raw in raw_results:
                parsed = self._parse_result(raw)
                if not parsed:
                    continue
                sid = parsed.get('source_id', '')
                if sid and sid in seen_ids:
                    continue
                if sid:
                    seen_ids.add(sid)
                parsed['source'] = self.source_name
                results.append(parsed)

            if not has_more:
                break
            kwargs['page'] = kwargs.get('page', 1) + 1

        logger.info(f'{self.source_name}: fetched {len(results)} results since {since_date}')
        return results

    def get_category(self, doc):
        """Map a document to a tracker category. Override for dynamic mapping."""
        return self.category


class MultiQuerySourceConnector(BaseSourceConnector):
    """Base for sources that run multiple search queries (CourtListener, NewsAPI).

    Subclasses must implement:
      - search_queries: list of query strings
      - _search(query, since_date): execute a single query, return raw results
      - _parse_result(raw): convert one result to a normalized dict
      - _get_id(raw): extract unique ID from a raw result for dedup
    """

    search_queries: list = []
    max_per_query: int = 20

    @abstractmethod
    def _search(self, query, since_date):
        """Execute a single search query. Returns list of raw results."""
        ...

    @abstractmethod
    def _get_id(self, raw) -> str:
        """Extract unique identifier from a raw result."""
        ...

    def _fetch_page(self, since_date, **kwargs):
        """Not used for multi-query connectors."""
        raise NotImplementedError

    def fetch_since(self, since_date, rate_limiter=None):
        """Fetch results across all search queries, deduplicating."""
        results = []
        seen_ids = set()

        for query in self.search_queries:
            if rate_limiter:
                rate_limiter.wait_if_needed(self.source_name)

            try:
                raw_results = self._search(query, since_date)
                for raw in raw_results[:self.max_per_query]:
                    rid = self._get_id(raw)
                    if rid in seen_ids:
                        continue
                    seen_ids.add(rid)

                    parsed = self._parse_result(raw)
                    if parsed:
                        parsed['source'] = self.source_name
                        results.append(parsed)
            except Exception as e:
                logger.warning(f'{self.source_name} query "{query[:50]}" failed: {e}')
                continue

        logger.info(f'{self.source_name}: fetched {len(results)} results since {since_date}')
        return results
