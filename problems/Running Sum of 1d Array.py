# https://leetcode.com/explore/challenge/card/may-leetcoding-challenge-2021/598/week-1-may-1st-may-7th/3730/

class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        runningsums = [nums[0]] + [None for _ in range(len(nums)-1)]
        
        for i in range(1, len(nums)):
            runningsums[i] = runningsums[i-1] + nums[i]
            
        return runningsums
