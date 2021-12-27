# https://leetcode.com/problems/insert-delete-getrandom-o1
# Medium

# List, dict (hashmap) combination

"""
Implement the RandomizedSet class:

RandomizedSet() Initializes the RandomizedSet object.

bool insert(int val) Inserts an item val into the set if not present. 
Returns true if the item was not present, false otherwise.

bool remove(int val) Removes an item val from the set if present. 
Returns true if the item was present, false otherwise.

int getRandom() Returns a random element from the current set of elements 
(it's guaranteed that at least one element exists when this method is called). 
Each element must have the same probability of being returned.

You must implement the functions of the class such that each function works in average O(1) time complexity.
"""

import random

class RandomizedSet:
    """For the required inserts and removes, a set is bueno.
    For random access not so much (or python version dependent).
    
    Anyway, lets do this more from scratch:
    lets use a list to store the values, and a dict that maps value to list index
    """

    def __init__(self):
        self.lst = []
        self.val_to_idx = dict()
        
        
    def insert(self, val: int) -> bool:
        if val in self.val_to_idx:
            return False
        
        # otherwise add
        self.lst.append(val)
        self.val_to_idx[val] = len(self.lst) - 1
        return True
        

    def remove(self, val: int) -> bool:
        if val not in self.val_to_idx:
            return False
        
        # else remove
        # put the last element to that location in array, and update val_to_idx mapping
        remove_idx = self.val_to_idx[val]
        self.lst[remove_idx] = self.lst[-1]
        self.val_to_idx[self.lst[-1]] = remove_idx
        
        # remove stuff
        self.lst.pop()
        del self.val_to_idx[val]
        return True
        

    def getRandom(self) -> int:
        # random(): generates a random float uniformly in the semi-open range [0.0, 1.0)
        return self.lst[int(random.random() * len(self.lst))]


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()
