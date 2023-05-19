#!/usr/bin/env python3
'''
File: 4-mru_cache.py
'''

BaseCaching = __import__("base_caching").BaseCaching


class MRUCache(BaseCaching):
    '''inherits from BaseCaching and is a MRU caching system'''
    def __init__(self):
        """ Initialize MRUCache """
        super().__init__()
        self.usage_order = []

    def put(self, key, item):
        """ Add an item in the cache """
        if key is None or item is None:
            return

        if key in self.cache_data:
            self.usage_order.remove(key)
        elif len(self.cache_data) >= self.MAX_ITEMS:
            mru_key = self.usage_order.pop()
            del self.cache_data[mru_key]
            print("DISCARD:", mru_key)

        self.cache_data[key] = item
        self.usage_order.append(key)

    def get(self, key):
        """ Get an item by key """
        if key is None or key not in self.cache_data:
            return None

        self.usage_order.remove(key)
        self.usage_order.append(key)

        return self.cache_data[key]
