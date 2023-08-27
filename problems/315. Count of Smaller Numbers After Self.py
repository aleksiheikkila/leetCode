""" 
315. Count of Smaller Numbers After Self
Hard

You are given an integer array nums and you have to return a new counts array. 
The counts array has the property where counts[i] is the number of smaller elements to the right of nums[i].

Aproaches:
1) BinaryIndexTree
2) SortedList

"""

from typing import List
from sortedcontainers import SortedList


class BinaryIndexTree():
    def __init__(self, n):
        self.nums = [0] * (n+1)
        
    def query(self, i):
        res = 0
        while i > 0:
            res += self.nums[i]
            i -= (i & -i)
        return res
    
    def update(self, i, v):  # v is delta
        while i < len(self.nums):
            self.nums[i] += v
            i += (i & -i)
            

class Solution:
    def countSmaller_binaryindextree(self, nums: List[int]) -> List[int]:
        """ Based on BIT.
        Time complexity NlogN
        """
        e = {v: i for i, v in enumerate(sorted(set(nums)))}
        b = BinaryIndexTree(len(e))
        rst = []
        indexes = [e[n] for n in nums]
        
        for i in indexes[::-1]:
            rst.append(b.query(i))
            b.update(i+1, 1)

        return rst[::-1]
            
    
    def countSmaller(self, nums: List[int]) -> List[int]:
        """ Based on SortedList.
        Time complexity NlogN
        """
        rst = []
        sl = SortedList()
        # adding value: log(N)
        # bisecting: log(N)
        
        for num in nums[::-1]:
            rst.append(sl.bisect_left(num))
            sl.add(num)
            
        return rst[::-1]
