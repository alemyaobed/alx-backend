#!/usr/bin/env python3
'''
Create a class LRUCache that inherits from BaseCaching and is a caching system:

You must use self.cache_data - dictionary from the parent class BaseCaching
You can overload def __init__(self): but don’t forget to call the parent init: super().__init__()
def put(self, key, item):
Must assign to the dictionary self.cache_data the item value for the key key.
If key or item is None, this method should not do anything.
If the number of items in self.cache_data is higher that BaseCaching.MAX_ITEMS:
you must discard the least recently used item (LRU algorithm)
you must print DISCARD: with the key discarded and following by a new line
def get(self, key):
Must return the value in self.cache_data linked to key.
If key is None or if the key doesn’t exist in self.cache_data, return None.
'''
from base_caching import BaseCaching


class LRUCache(BaseCaching):
    ''''''
    def __init__(self):
        ''' Initialize the LRUCache instance '''
        super().__init__()
        self.hits = {}
    
    def put(self, key, item):
        '''Adding items to the dictionary using the LRU algorithm'''
        if key and item:
            if key in self.cache_data:
                self.cache_data[key] = item
            else:
                if len(self.cache_data) == BaseCaching.MAX_ITEMS:
                    # Getting all the number of hits for each key to find the least
                    all_hits = [value for _, value in self.hits.items()]
                    # Getting the least hit key
                    least_hit_key = self.get_hit_key(min(all_hits))
                
                    print("DISCARD: {}".format(least_hit_key))
                    # Deleteing the item using the key
                    del self.cache_data[least_hit_key]
                    del self.hits[least_hit_key]
                    
                self.cache_data[key] = item
                self.hits[key] = 0
    
    def get_hit_key(self, item):
        """ Get the key associated with an item with least hits"""
        for key, value in self.hits.items():
            if value == item:
                return key
        return None
        
    
    def get(self, key):
        '''Get an item by key'''
        # Checking if the key is not None
        if key:
            result = self.cache_data.get(key)
            if result:
                # Incrementing the hit for that key
                self.hits[key] += 1
                return result
        return None
