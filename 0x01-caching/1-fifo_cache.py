#!/usr/bin/env python3
""" FIFO caching system
"""

from base_caching import BaseCaching


class FIFOCache(BaseCaching):
    """FIFO caching algorithm"""
    def __init__(self):
        """initialization method"""
        super().__init__()
        self.keys = []

    def put(self, key, item):
        """ Add an item in the cache
        """
        if key is not None and item is not None:
            if len(self.cache_data) >= self.MAX_ITEMS:
                if self.keys:
                    discard_key = self.keys.pop(0)
                    del self.cache_data[discard_key]
                    print("DISCARD:", discard_key)

        self.cache_data[key] = item
        self.keys.append(key)

    def get(self, key):
        """ Get an item by key
        """
        if key is not None:
            return self.cache_data.get(key)
