#!/usr/bin/env python3
'''
Create a class MRUCache that inherits from BaseCaching and is a
caching system:

You must use self.cache_data - dictionary from the parent class BaseCaching
You can overload def __init__(self): but don’t forget to call the parent init:
super().__init__()
def put(self, key, item):
Must assign to the dictionary self.cache_data the item value for the key key.
If key or item is None, this method should not do anything.
If the number of items in self.cache_data is higher that BaseCaching.MAX_ITEMS:
you must discard the most recently used item (MRU algorithm)
you must print DISCARD: with the key discarded and following by a new line
def get(self, key):
Must return the value in self.cache_data linked to key.
If key is None or if the key doesn’t exist in self.cache_data, return None.
'''
from base_caching import BaseCaching


class MRUCache(BaseCaching):
    """
    MRUCache class that inherits from BaseCaching and implements MRU caching
    """

    def __init__(self):
        """Initialize the LRUCache instance"""
        super().__init__()
        self.mru_order = []

    def put(self, key, item):
        """Add an item in the cache using the LRU algorithm"""
        if key is not None and item is not None:
            if key in self.cache_data:
                # If key is already in cache, remove it to update its position
                self.mru_order.remove(key)
            elif len(self.cache_data) >= BaseCaching.MAX_ITEMS:
                # If cache is full, discard the least recently used item
                mru_key = self.mru_order.pop()
                print("DISCARD: {}".format(mru_key))
                del self.cache_data[mru_key]

            # Add the new item to the cache and update LRU order
            self.cache_data[key] = item
            self.mru_order.append(key)

    def get(self, key):
        """Get an item by key"""
        if key is None or key not in self.cache_data:
            return None

        # Move the accessed item to the end of the LRU order
        self.mru_order.remove(key)
        self.mru_order.append(key)
        return self.cache_data[key]
