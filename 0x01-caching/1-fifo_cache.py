#!/usr/bin/env python3
'''
1-fifo_cache.py
'''

BaseCaching = __import__("base_caching").BaseCaching


class FIFOCache(BaseCaching):
    '''inherits from BaseCaching and is a FIFO caching system'''
    def __init__(self):
        ''' Initialize FIFOCache '''
        super().__init__()
        self.queue = []

    def put(self, key, item):
        ''' Add an item in the cache '''
        if key is None or item is None:
            return

        if len(self.cache_data) >= self.MAX_ITEMS:
            if key not in self.cache_data:
                discard_key = self.queue.pop(0)
                del self.cache_data[discard_key]
                print("DISCARD:", discard_key)

        self.cache_data[key] = item
        self.queue.append(key)

    def get(self, key):
        ''' Get an item by key '''
        if key is None or key not in self.cache_data:
            return None
        return self.cache_data[key]
