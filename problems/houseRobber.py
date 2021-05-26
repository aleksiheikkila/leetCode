class Solution:
    def rob(self, nums: List[int]) -> int:
        prevMax = 0
        currMax = 0
        
        # example nums: [10, 20, 2, 3, 50, 15] -->
        # rolling loot = 10, 20, 20, 23, 70, 70
        
        for num in nums:
            prevMax, currMax = currMax, max(prevMax + num, currMax)
            print(prevMax, currMax)
         
        return currMax
    