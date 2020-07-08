"""
Design a HashMap without using any built-in hash table libraries.

To be specific, your design should include these functions:
put(key, value) : Insert a (key, value) pair into the HashMap. If the value already exists in the HashMap, update the value.
get(key): Returns the value to which the specified key is mapped, or -1 if this map contains no mapping for the key.
remove(key) : Remove the mapping for the value key if this map contains the mapping for the key.

Note:
All keys and values will be in the range of [0, 1000000].
The number of operations will be in the range of [1, 10000].
Please do not use the built-in HashMap library.
"""

# first solution just uses an array with the a length of the maximum key value called + 1 (with values of None to fill space)
# class MyHashMap:

#     def __init__(self):
#         """
#         Initialize your data structure here.
#         """
#         self.map = []

#     def put(self, key: int, value: int) -> None:
#         """
#         value will always be non-negative.
#         """
#         if len(self.map) < key + 1:
#             self.map += [None]*(key + 1 - len(self.map))
#         self.map[key] = value

#     def get(self, key: int) -> int:
#         """
#         Returns the value to which the specified key is mapped, or -1 if this map contains no mapping for the key
#         """
#         if len(self.map) >= key + 1:
#             return self.map[key] if self.map[key] != None else -1
#         return -1

#     def remove(self, key: int) -> None:
#         """
#         Removes the mapping of the specified value key if this map contains a mapping for the key
#         """
#         if key + 1 == len(self.map):
#             self.map.pop()
#         elif key + 1 < len(self.map):
#             self.map[key] = None

# created a chained hash map with an adjustable size
class ListNode:
    def __init__(self, key, value):
        self.pair = (key, value)
        self.next = None

class MyHashMap:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.size = 1000
        self.map = [None]*self.size

    def put(self, key: int, value: int) -> None:
        """
        value will always be non-negative.
        """
        index = key % self.size
        if self.map[index] == None:
            self.map[index] = ListNode(key, value)
        else:
            runner = self.map[index]
            while runner != None:
                if runner.pair[0] == key:
                    runner.pair = (key, value)
                    return
                if runner.next == None: 
                    break
                runner = runner.next
            runner.next = ListNode(key, value)

    def get(self, key: int) -> int:
        """
        Returns the value to which the specified key is mapped, or -1 if this map contains no mapping for the key
        """
        index = key % self.size
        runner = self.map[index]
        while runner != None:
            if runner.pair[0] == key:
                return runner.pair[1]
            runner = runner.next
        return -1

    def remove(self, key: int) -> None:
        """
        Removes the mapping of the specified value key if this map contains a mapping for the key
        """
        index = key % self.size
        runner = self.map[index]
        if runner == None:
            return
        if runner.pair[0] == key:
            self.map[index] = runner.next
            return
        while runner != None:
            if runner.next and runner.next.pair[0] == key:
                runner.next = runner.next.next
            runner = runner.next

obj = MyHashMap()
obj.put(1, 1)          
obj.put(2, 2)         
print(obj.get(1))            # returns 1
print(obj.get(3))            # returns -1 (not found)
obj.put(2, 1)                # update the existing value
print(obj.get(2))            # returns 1 
obj.remove(2)                # remove the mapping for 2
print(obj.get(2))            # returns -1 (not found) 