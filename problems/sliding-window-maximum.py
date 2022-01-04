# https://leetcode.com/problems/sliding-window-maximum
# HARD


""" Problem:
You are given an array of integers nums, there is a sliding window of size k 
which is moving from the very left of the array to the very right. 
You can only see the k numbers in the window. 
Each time the sliding window moves right by one position.

Return the max sliding window.

##############
Approach:

deque containing some of the indices for the window.
where the leftmost value (index) corresponds to the largest num within the window,

One by one, process the nums.

Add num (index) to deque right. 
First pop index values from right as long as they correspond to a num smaller than the current.
(Those earlier values that are smaller wont be the max of any window still to come).

Remove index from left side of the deque if it has fallen out of the window.

When we have reached the full window lenght, start adding maximums to the output.
The index to the max value will be found at the deque position zero.
"""

from typing import List
from collections import deque


class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        result = []
        left = right = 0  # pointer to the first and last index of the window
        queue = deque()
        
        while right < len(nums):
            
            # get rid of the index that falls out of the window 
            if queue and left > queue[0]:
                queue.popleft()
                
            # add new value, but first get rid of all smaller ones
            new_val = nums[right]
            # get rid of all the prior smaller values
            while queue and nums[queue[-1]] < new_val:
                queue.pop()
            # then add the new index to the right
            queue.append(right)
            
            # add max window value to result (only when we have reached full window)
            # and increment left pointer
            if (right + 1) >= k:
                result.append(nums[queue[0]])
                left += 1
            
            # always increment right pointer as we step
            right += 1
            
        return result
        