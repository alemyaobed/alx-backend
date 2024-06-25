#!/usr/bin/env python3
'''
Create a class LIFOCache that inherits from BaseCaching and is a caching
system:

You must use self.cache_data - dictionary from the parent class BaseCaching
You can overload def __init__(self): but don’t forget to call the parent init:
super().__init__()
def put(self, key, item):
Must assign to the dictionary self.cache_data the item value for the key key.
If key or item is None, this method should not do anything.
If the number of items in self.cache_data is higher that BaseCaching.MAX_ITEMS:
you must discard the last item put in cache (LIFO algorithm)
you must print DISCARD: with the key discarded and following by a new line
def get(self, key):
Must return the value in self.cache_data linked to key.
If key is None or if the key doesn’t exist in self.cache_data, return None.
'''
from base_caching import BaseCaching


class LIFOCache(BaseCaching):
    '''Defines a LIFO caching system'''
    def __init__(self):
        '''Initialize the FIFOCache instance'''
        super().__init__()

    def put(self, key, item):
        '''Adding items to the dictionary using the LIFO algorithm'''
        if key and item:
            if len(self.cache_data) == BaseCaching.MAX_ITEMS:
                # Getting all keys by iterating and storing the keys
                keys = [key for key, _ in self.cache_data.items()]
                # Getting the key
                key_last = keys[-1]
                print("DISCARD: {}".format(key_last))
                # Deleteing the item using the key
                del self.cache_data[key_last]
            self.cache_data[key] = item

    ###################################################################
    # A SMARTER WAY AS OPPOSED TO ITERATING
    ###################################################################
    # def __init__(self):
    #     """ Initialize the LIFOCache instance """
    #     super().__init__()
    #     self.last_key = None  # To keep track of the last added key

    # def put(self, key, item):
    #     """ Add an item in the cache """
    #     if key is None or item is None:
    #         return

    #     # If the cache is full, remove the last added item
    #     if len(self.cache_data) >= self.MAX_ITEMS:
    #         if self.last_key is not None:
    #             print(f"DISCARD: {self.last_key}")
    #             del self.cache_data[self.last_key]

    #     # Add the new item to cache
    #     self.cache_data[key] = item
    #     self.last_key = key

    def get(self, key):
        '''Get an item by key'''
        # Checking if the key is not None
        if key:
            result = self.cache_data.get(key)
            if result:
                return result
        return None
