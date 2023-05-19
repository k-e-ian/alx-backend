#!/usr/bin/env python3
'''
File: 100-lfu_cache.py
'''
from collections import defaultdict

BaseCaching = __import__("base_caching").BaseCaching


class LFUCache(BaseCaching):
    def __init__(self):
        """ Initialize LFUCache """
        super().__init__()
        self.frequency = defaultdict(int)
        self.min_frequency = 0

    def put(self, key, item):
        """ Add an item in the cache """
        if key is None or item is None:
            return

        if key in self.cache_data:
            self.cache_data[key] = item
            self.frequency[key] += 1
        else:
            if len(self.cache_data) >= self.MAX_ITEMS:
                min_freq_keys = [
                    k for k in self.cache_data
                    if self.frequency[k] == self.min_frequency
                ]
                lru_key = min_freq_keys.pop(0)
                del self.cache_data[lru_key]
                del self.frequency[lru_key]
                print("DISCARD:", lru_key)

            self.cache_data[key] = item
            self.frequency[key] = 1
            self.min_frequency = 1

    def get(self, key):
        """ Get an item by key """
        if key is None or key not in self.cache_data:
            return None

        self.frequency[key] += 1

        return self.cache_data[key]
