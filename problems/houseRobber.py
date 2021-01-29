class Solution:
    def rob(self, nums: List[int]) -> int:
        prevMax = 0
        currMax = 0
        
        for num in nums:
            prevMax, currMax = currMax, max(prevMax + num, currMax)
            print(prevMax, currMax)
         
        return currMax
    