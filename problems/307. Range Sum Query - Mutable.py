""" 
307. Range Sum Query - Mutable
Medium
https://leetcode.com/problems/range-sum-query-mutable/

Given an integer array nums, handle multiple queries of the following types:

Update the value of an element in nums.
Calculate the sum of the elements of nums between indices left and right inclusive where left <= right.
Implement the NumArray class:

NumArray(int[] nums) Initializes the object with the integer array nums.
void update(int index, int val) Updates the value of nums[index] to be val.
int sumRange(int left, int right) Returns the sum of the elements of nums between indices left and right inclusive 
(i.e. nums[left] + nums[left + 1] + ... + nums[right]).
"""

from tkinter import N
from typing import List

class NumArray_slow:
    """ Naive, straightforward. It is too slow --> Time Limit Exceeded.
    
    Alternatives: cumulative sum array --> still slow for updates as the rest of the cumsum array needs to be updated
    Binary Indexed Tree BIT is a good choice"""

    def __init__(self, nums: List[int]):
        self.nums = nums.copy()
        

    def update(self, index: int, val: int) -> None:
        self.nums[index] = val
        

    def sumRange(self, left: int, right: int) -> int:
        return sum(self.nums[left:right+1])
        


class BIT:
    def __init__(self, n: int):
        # BIT is one-indexed
        self.sums = [0] * (n + 1)


    def update(self, index: int, val):  # val is the delta value
        while index < len(self.sums):
            self.sums[index] += val
            index += (index & -index)
            

    def query(self, index: int):
        res = 0
        while index > 0:
            res += self.sums[index]
            # remove the rightmost set bit
            # substract the (AND with 2s complement) 
            index -= (index & -index)
        return res



class NumArray:
    """ Naive, straightforward. It is too slow --> Time Limit Exceeded.
    
    Alternatives: cumulative sum array --> still slow for updates as the rest of the cumsum array needs to be updated
    Binary Indexed Tree BIT is a good choice"""

    def __init__(self, nums: List[int]):
        self.nums = nums.copy()
        self.bit = BIT(len(nums))
        for i, v in enumerate(self.nums):
            # inited to zeros, so v's are the delta
            self.bit.update(i+1, v)
        

    def update(self, index: int, val: int) -> None:
        delta = val - self.nums[index]
        self.bit.update(index+1, delta)
        self.nums[index] = val
        

    def sumRange(self, left: int, right: int) -> int:
        return self.bit.query(right+1) - self.bit.query(left)  # i.e (cumsum to right) - (cumsum to left-1)
        

# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# obj.update(index,val)
# param_2 = obj.sumRange(left,right)
