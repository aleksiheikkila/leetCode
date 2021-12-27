# https://leetcode.com/problems/insert-delete-getrandom-o1-duplicates-allowed
# Hard

"""
RandomizedCollection is a data structure that contains a collection of numbers, 
possibly duplicates (i.e., a multiset). 
It should support inserting and removing specific elements and also removing a random element.

Implement the RandomizedCollection class:

RandomizedCollection() Initializes the empty RandomizedCollection object.

bool insert(int val) Inserts an item val into the multiset, even if the item is already present. 
Returns true if the item is not present, false otherwise.

bool remove(int val) Removes an item val from the multiset if present. 
Returns true if the item is present, false otherwise. 
Note that if val has multiple occurrences in the multiset, we only remove one of them.

int getRandom() Returns a random element from the current multiset of elements. 
The probability of each element being returned is linearly related to the number 
of same values the multiset contains.
You must implement the functions of the class such that each function works on average O(1) time complexity.

Note: The test cases are generated such that getRandom will only be called if 
there is at least one item in the RandomizedCollection.
"""

from collections import defaultdict
import random


class RandomizedCollection:

    def __init__(self):
        self.lst = []
        self.val_to_idx = defaultdict(list)
        
    
    def insert(self, val: int) -> bool:
        is_new_val = len(self.val_to_idx[val]) == 0
    
        # add in any case
        self.lst.append(val)
        self.val_to_idx[val].append(len(self.lst) - 1)
        
        return is_new_val
        

    def remove(self, val: int) -> bool:
        if len(self.val_to_idx[val]) == 0:
            return False
        
        # else remove
        # put the last element to that location in array, and update val_to_idx mapping
        remove_idx = self.val_to_idx[val].pop()  # get the last index
        
        # Housekeeping: remove empty list from the mapping
        if len(self.val_to_idx[val]) == 0:
            del self.val_to_idx[val]
        
        last_idx = len(self.lst) - 1
        # if we are not removing the last element
        if remove_idx < last_idx:
            last_val = self.lst[-1]
            last_val_mapping = self.val_to_idx[last_val]
            self.lst[remove_idx] = last_val
            
            # Update the last_val to list index mapping:
            # change the last idx to the new location, i.e. remove_idx
            for i in range(len(last_val_mapping)-1, -1, -1):
                # tends(?) to typically be closer to the end, so do it in reverse order
                if last_val_mapping[i] == last_idx:
                    last_val_mapping[i] = remove_idx
                    break

        # remove stuff
        self.lst.pop()

        return True
        

    def getRandom(self) -> int:
        # random(): generates a random float uniformly in the semi-open range [0.0, 1.0)
        return self.lst[int(random.random() * len(self.lst))]
        

# Your RandomizedCollection object will be instantiated and called as such:
# obj = RandomizedCollection()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()
