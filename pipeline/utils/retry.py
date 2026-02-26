"""Retry logic with exponential backoff."""
import time
import functools
import logging

logger = logging.getLogger('tckc_pipeline')


def retry_with_backoff(max_retries=3, base_delay=2, max_delay=60, exceptions=(Exception,)):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            for attempt in range(max_retries + 1):
                try:
                    return func(*args, **kwargs)
                except exceptions as e:
                    if attempt == max_retries:
                        logger.error(f'{func.__name__} failed after {max_retries} retries: {e}')
                        raise
                    delay = min(base_delay * (2 ** attempt), max_delay)
                    logger.warning(f'{func.__name__} attempt {attempt + 1} failed: {e}. Retrying in {delay}s')
                    time.sleep(delay)
        return wrapper
    return decorator
