#!/usr/bin/env python3
'''
2-lifo_cache.py
'''

BaseCaching = __import__("base_caching").BaseCaching


class LIFOCache(BaseCaching):
    '''inherits from BaseCaching and is a LIFO caching system'''
    def __init__(self):
        """ Initialize LIFOCache """
        super().__init__()
        self.stack = []

    def put(self, key, item):
        """ Add an item in the cache """
        if key is None or item is None:
            return

        if len(self.cache_data) >= self.MAX_ITEMS:
            if key not in self.cache_data:
                discard_key = self.stack.pop()
                del self.cache_data[discard_key]
                print("DISCARD:", discard_key)

        self.cache_data[key] = item
        self.stack.append(key)

    def get(self, key):
        """ Get an item by key """
        if key is None or key not in self.cache_data:
            return None
        return self.cache_data[key]
