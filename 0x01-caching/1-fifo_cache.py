#!/usr/bin/env python3
'''
Create a class FIFOCache that inherits from BaseCaching and is a caching
system:

You must use self.cache_data - dictionary from the parent class BaseCaching
You can overload def __init__(self): but don’t forget to call the parent init:
super().__init__()
def put(self, key, item):
Must assign to the dictionary self.cache_data the item value for the key key.
If key or item is None, this method should not do anything.
If the number of items in self.cache_data is higher that BaseCaching.MAX_ITEMS:
you must discard the first item put in cache (FIFO algorithm)
you must print DISCARD: with the key discarded and following by a new line
def get(self, key):
Must return the value in self.cache_data linked to key.
If key is None or if the key doesn’t exist in self.cache_data, return None.
'''
from base_caching import BaseCaching


class FIFOCache(BaseCaching):
    '''
    Defines a FIFO caching system
    '''
    def __init__(self):
        '''Initialize the FIFOCache instance'''
        super().__init__()

    def put(self, key, item):
        '''Adding items to the dictionary using the FIFO algorithm'''
        if key and item:
            if len(self.cache_data) == BaseCaching.MAX_ITEMS:
                # Getting the key using iter and next
                key_first = next(iter(self.cache_data))
                print("DISCARD: {}".format(key_first))
                # Deleteing the item using the key
                del self.cache_data[key_first]
            self.cache_data[key] = item

    def get(self, key):
        '''Get an item by key'''
        # Checking if the key is not None
        if key:
            result = self.cache_data.get(key)
            if result:
                return result
        return None
