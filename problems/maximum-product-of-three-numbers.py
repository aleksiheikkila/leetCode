# https://leetcode.com/problems/maximum-product-of-three-numbers

#import operator
#import functools

#def prod(nums):
#    return functools.reduce(operator.mul, nums, 1)

class Solution:
    def maximumProduct(self, nums: List[int]) -> int:
        nums.sort()

        # either multiply the three largest values together, or
        # the largest value and the two smallest (case the two smallest are both negative)
        
        return max(nums[-1] * nums[-2] * nums[-3],
                   nums[0]  * nums[1]  * nums[-1])
