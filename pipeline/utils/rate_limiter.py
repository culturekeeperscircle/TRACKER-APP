"""Rate limiting for API calls."""
import time
from datetime import datetime, timedelta
from collections import defaultdict


class RateLimiter:
    def __init__(self):
        self.calls = defaultdict(list)
        self.limits = {
            'federal_register': {'per_hour': 500},
            'congress_gov': {'per_hour': 5000},
            'courtlistener': {'per_hour': 5000},
            'news_api': {'per_day': 100},
            'anthropic': {'per_minute': 50},
        }

    def wait_if_needed(self, source):
        config = self.limits.get(source, {})
        now = datetime.now()

        if 'per_minute' in config:
            cutoff = now - timedelta(minutes=1)
            self.calls[source] = [t for t in self.calls[source] if t > cutoff]
            if len(self.calls[source]) >= config['per_minute']:
                sleep_time = (self.calls[source][0] - cutoff).total_seconds() + 0.5
                time.sleep(max(0, sleep_time))

        elif 'per_hour' in config:
            cutoff = now - timedelta(hours=1)
            self.calls[source] = [t for t in self.calls[source] if t > cutoff]
            if len(self.calls[source]) >= config['per_hour']:
                sleep_time = (self.calls[source][0] - cutoff).total_seconds() + 0.5
                time.sleep(max(0, sleep_time))

        elif 'per_day' in config:
            cutoff = now - timedelta(days=1)
            self.calls[source] = [t for t in self.calls[source] if t > cutoff]
            if len(self.calls[source]) >= config['per_day']:
                sleep_time = (self.calls[source][0] - cutoff).total_seconds() + 0.5
                time.sleep(max(0, sleep_time))

        self.calls[source].append(datetime.now())
