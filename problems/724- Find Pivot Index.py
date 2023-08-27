""" 
724. Find Pivot Index
EASY
https://leetcode.com/problems/find-pivot-index

Given an array of integers nums, calculate the pivot index of this array.

The pivot index is the index where the sum of all the numbers strictly to the left of the index is equal to the sum of all the numbers strictly to the index's right.

If the index is on the left edge of the array, then the left sum is 0 because there are no elements to the left. This also applies to the right edge of the array.

Return the leftmost pivot index. If no such index exists, return -1.

"""

class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        left_sum = 0
        right_sum = sum(nums)

        for i in range(len(nums)):
            if i > 0:
                left_sum += nums[i-1]
            right_sum -= nums[i]

            if right_sum == left_sum:
                return i

        return -1
