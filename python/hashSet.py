"""
Design a HashSet without using any built-in hash table libraries.

To be specific, your design should include these functions:
add(value): Insert a value into the HashSet. 
contains(value) : Return whether the value exists in the HashSet or not.
remove(value): Remove a value in the HashSet. If the value does not exist in the HashSet, do nothing.

Note:
All values will be in the range of [0, 1000000].
The number of operations will be in the range of [1, 10000].
Please do not use the built-in HashSet library.
"""

class MyHashSet:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.c = [11, 23, 53, 103, 251, 503, 1009, 2503, 5003, 7001, 13339] #capacity (prime numbers up to ~ 13,000 bc of 1.3*10,000 max operations in problem desc)
        self.i = 0 #index for capacity array
        self.s = 0 #current size
        self.h = [None] * self.c[self.i]
        self.lf = float(3)/4 #load factor

    def hash1(self, key: int) -> int:
        return key % self.c[self.i]
    
    def hash2(self, key: int) -> int:
        return 1 + key % (self.c[self.i] - 1)
    
    def add(self, key: int) -> None:
        # if the current size is >= the capacity * the load factor, increase the capacity, create a new list, and rehash
        if self.s >= self.c[self.i] * self.lf:
            self.i += 1
            n = [None]*self.c[self.i]
            for j in range(self.c[self.i - 1]):
                if self.h[j] and self.h[j] != -1:
                    k = self.h[j]
                    i = 0
                    h1 = index = self.hash1(k)
                    h2 = self.hash2(k)
                    while n[index] is not None:
                        i += 1
                        index = (h1 + i*h2) % self.c[self.i]
                    n[index] = k
            self.h = n
        i = 0
        h1 = index = self.hash1(key)
        h2 = self.hash2(key)
        deleted = []
        # searching through current hash set
        while self.h[index] is not None:
            # if the key is already present, do nothing
            if self.h[index] == key:
                return
            # if a deleted element is found, store the index (cannot break the loop here in case the key is already present after a deleted element)
            if self.h[index] == -1:
                deleted.append(index)
            i += 1
            index = (h1 + i*h2) % self.c[self.i]
        # if the search ends, the key was not found to be present, and there is a deleted index to fill, use the deleted index instead of the empty index
        if self.h[index] is None and deleted:
            index = deleted[0]
        # insert the key into the first empty index or deleted index
        self.h[index] = key
        self.s += 1

    def remove(self, key: int) -> None:
        i = 0
        h1 = index = self.hash1(key)
        h2 = self.hash2(key)
        while self.h[index] is not None:
            if self.h[index] == key:
                # -1 used to signify a deleted element
                self.h[index] = -1
                self.s -= 1
                return
            i += 1
            index = (h1 + i*h2) % self.c[self.i]

    def contains(self, key: int) -> bool:
        """
        Returns true if this set contains the specified element
        """
        i = 0
        h1 = index = self.hash1(key)
        h2 = self.hash2(key)
        while self.h[index] != None:
            if self.h[index] == key:
                return True
            i += 1
            index = (h1 + i*h2) % self.c[self.i]
        return False

import unittest

class hashSetTest(unittest.TestCase):
    def setUp(self):
        self.obj = MyHashSet()

    def test1(self):
        self.obj.add(1)         
        self.obj.add(6)   
        self.assertEqual(self.obj.contains(1), True)
        self.obj.add(26)
        self.obj.add(26)
        self.assertEqual(self.obj.h, [None, 1, 26, None, 6])
        self.obj.remove(6) 
        self.assertEqual(self.obj.contains(6), False)
        self.obj.add(6)
        self.assertEqual(self.obj.h, [None, 1, 26, None, 6])
        self.obj.add(5)
        self.obj.add(123)
        self.assertEqual(self.obj.i, 1)
        self.assertEqual(self.obj.contains(123), True)

if __name__ == '__main__':
    unittest.main()