#!/usr/bin/env python3
'''
File: 100-lfu_cache.py
'''
from collections import defaultdict

BaseCaching = __import__("base_caching").BaseCaching


class LFUCache(BaseCaching):
    '''inherits from BaseCaching and is a LFU caching system'''
    def __init__(self):
        """ Initialize LFUCache """
        super().__init__()
        self.frequency = defaultdict(int)
        self.min_frequency = 0

    def put(self, key, item):
        """ Add an item to the cache using LFU algorithm """
        if key is None or item is None:
            return

        if key in self.cache_data:
            self.cache_data[key] = item
            self.frequency[key] += 1
        else:
            if len(self.cache_data) >= BaseCaching.MAX_ITEMS:
                min_freq_keys = [
                    k for k in self.cache_data
                    if self.frequency[k] == self.min_frequency]
                if len(min_freq_keys) > 1:
                    lru_key = min(min_freq_keys,
                                  key=lambda k: self.cache_data[k])
                    self.cache_data.pop(lru_key)
                    del self.frequency[lru_key]
                    print("DISCARD:", lru_key)
                else:
                    lfu_key = min_freq_keys[0]
                    self.cache_data.pop(lfu_key)
                    del self.frequency[lfu_key]
                    print("DISCARD:", lfu_key)

            self.cache_data[key] = item
            self.frequency[key] = 1
            self.min_frequency = 1 if not self.min_frequency else min(self.frequency.values())

    def get(self, key):
        """ Get an item by key """
        if key is None or key not in self.cache_data:
            return None

        self.frequency[key] += 1

        return self.cache_data[key]
