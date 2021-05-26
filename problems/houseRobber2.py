# https://leetcode.com/problems/house-robber-ii/

# as the first value, but now the houses are in a circle, i.e. first and last elem are neighbors
# as before, but cannot rob first and last house at the same time
# Therefore, max(rob1(houses1... n), rob1(houses0... n-1))

class Solution:
    def rob1(self, nums: List[int]) -> int:
        """This was the solution for the houseRobber.py - the linear case"""
        prevMax = 0
        currMax = 0
        # example nums: [10, 20, 2, 3, 50, 15] -->
        # rolling loot = 10, 20, 20, 23, 70, 70
        
        for num in nums:
            prevMax, currMax = currMax, max(prevMax + num, currMax)
            print(prevMax, currMax)
         
        return currMax

    
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0
        elif len(nums) == 1:
            return nums[0]
        else:
            return max(self.rob1(nums[:-1]), self.rob1(nums[1:]))
    