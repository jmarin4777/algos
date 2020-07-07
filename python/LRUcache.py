"""
Design and implement a data structure for Least Recently Used (LRU) cache. It should support the following operations: get and put.

get(key) - Get the value (will always be positive) of the key if the key exists in the cache, otherwise return -1.
put(key, value) - Set or insert the value if the key is not already present. When the cache reached its capacity, it should invalidate the least recently used item before inserting a new item.

The cache is initialized with a positive capacity.
"""

from collections import OrderedDict

class LRUCache:

    def __init__(self, capacity: int):
        self.cache = OrderedDict()
        self.capacity = capacity
        
    def get(self, key: int) -> int:
        if key in self.cache:
            temp = self.cache[key]
            del self.cache[key]
            self.cache[key] = temp
            return temp
        return -1

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            del self.cache[key]
        else:
            if len(self.cache) == self.capacity:
                self.cache.popitem(False)
        self.cache[key] = value

obj = LRUCache(2)
obj.put(1, 1)
obj.put(2, 2)
print(obj.get(1))       # returns 1
obj.put(3, 3)    # evicts key 2
print(obj.get(2))       # returns -1 (not found)
obj.put(4, 4)    # evicts key 1
print(obj.get(1))       # returns -1 (not found)
print(obj.get(3))       # returns 3
print(obj.get(4))       # returns 4
