#!/usr/bin/env python3
"""
Create a class LFUCache that inherits from BaseCaching and is a
caching system:

You must use self.cache_data - dictionary from the parent class BaseCaching
You can overload def __init__(self): but don’t forget to call the parent init:
super().__init__()
def put(self, key, item):
Must assign to the dictionary self.cache_data the item value for the key key.
If key or item is None, this method should not do anything.
If the number of items in self.cache_data is higher that BaseCaching.MAX_ITEMS:
you must discard the least frequency used item (LFU algorithm)
if you find more than 1 item to discard, you must use the LRU algorithm
to discard only the least recently used
you must print DISCARD: with the key discarded and following by a new line
def get(self, key):
Must return the value in self.cache_data linked to key.
If key is None or if the key doesn’t exist in self.cache_data, return None.
"""
from base_caching import BaseCaching
from collections import OrderedDict, defaultdict


class LFUCache(BaseCaching):
    """
    LFUCache class that inherits from BaseCaching and implements LFU caching
    """
    def __init__(self):
        """Initialize the LFUCache instance"""
        super().__init__()
        self.freq = defaultdict(int)  # To track frequency of keys
        self.order = OrderedDict()    # To track order of keys

    def put(self, key, item):
        """Adding items to the dictionary using the LFU algorithm"""
        if key is None or item is None:
            return

        if key in self.cache_data:
            self.cache_data[key] = item
            self.freq[key] += 1
            self.order.move_to_end(key)
        else:
            if len(self.cache_data) >= BaseCaching.MAX_ITEMS:
                # Find the LFU key(s)
                min_freq = min(self.freq.values())
                lfu_keys = [k for k, f in self.freq.items() if f == min_freq]

                # Use LRU to break ties among LFU keys
                lru_key = next(iter(k for k in self.order if k in lfu_keys))
                print("DISCARD: {}".format(lru_key))
                self.cache_data.pop(lru_key)
                self.freq.pop(lru_key)
                self.order.pop(lru_key)

            self.cache_data[key] = item
            self.freq[key] = 1
            self.order[key] = None

    def get(self, key):
        """Get an item by key"""
        if key is None or key not in self.cache_data:
            return None

        self.freq[key] += 1
        self.order.move_to_end(key)
        return self.cache_data[key]
