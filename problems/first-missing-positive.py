# https://leetcode.com/problems/first-missing-positive/
# HARD

"""
Given an unsorted integer array nums, return the smallest missing positive integer.

You must implement an algorithm that runs in O(n) time and uses constant extra space.
"""

# First missing positive is in the range [1, len(nums)+1]

class Solution:
    def firstMissingPositive_2(self, nums: List[int]) -> int:
        """
        Use array of length len(nums)+1 to track which values 1...len(nums)+1.

        This has runtime of O(N) but also memory of O(N), so mem does not fulfill the req.

        """
        N = len(nums)
        seen_array = [0 for _ in range(N)]  # index 0: have we seen value 1?
        
        for num in nums:
            if 0 < num <= N:
                seen_array[num - 1] = 1
                
        for idx, val in enumerate(seen_array):
            if val == 0:
                return idx + 1
        
        # else we have continuous series of positive integers, 
        # and the first missing must be the value len(nums) + 1
        return N + 1


    def firstMissingPositive(self, nums: List[int]) -> int:
        """ Similar idea than the previous one, now using a nice trick to cut down
        extra memory needs.

        Trick here is to use the original nums list to mark what values we have seen, 
        without losing the original values. We do this by adding list length to the value
        in that index. Modulo operator can bring back the original value when needed.

        This is O(N) runtime with constant memory consumption, as required
        """
        
        if not nums or len(nums) == 0:
            return 1
        

        # dummy value to make the logic easier
        nums.append(0)
        # nums[0] used to indicate whether we have seen value 1, 
        # nums[N] used to indicate whether we have seen value len(nums)+1
        
        N = len(nums)
        
        temp = nums[0]  # for detecting the edge case: "value 1 not seen"
       
        # Step 1: get rid of uninteresting values
        for i in range(N):
            if nums[i] < 0 or nums[i] > N:
                nums[i] = 0
                
        # Step 2: mark what we have seen in the original array
        # without losing the original values
        # add N when seen, use modulo to get back the original value
        for i in range(N):
            if nums[i] > 0:
                nums[nums[i]%N - 1] += N


        # Step 3: check what is the first missing positive integer value
        # edge case: we have not seen the value 1: nums[0] has not been updated
        if temp == nums[0]:
            return 1
                
        for i in range(N):
            # if the value is < N, we have not seen the corresponding integer
            # nums[i] "encodes" number i+1, so return i+1
            if nums[i] // N == 0:
                return i + 1
            
        # else the answer must be the last one
        return N


"""
Full example: input [3,4,-1,1]

=>
[3,4,0,1,0]     
[3,4,5,1,0]     
[3,4,5,6,0]  
[3,4,5,6,5] 
[8,4,5,6,5] 
[8,4,5,6,10] 

=> index 1 is the one we have not seen, i.e. value 2!
"""
        
        
        
        
        
        