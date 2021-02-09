# https://leetcode.com/explore/learn/card/fun-with-arrays/523/conclusion/3270/
# Slow 
class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        
        all_nums = set(range(1, len(nums) + 1))
        
        for num in nums:
            all_nums.discard(num)
            
        return list(all_nums)


    def findDisappearedNumbers_another(self, nums: List[int]) -> List[int]:
        # Even slower still...
        for i in range(len(nums)):
            idx = abs(nums[i]) - 1
            nums[idx] = -abs(nums[idx])
            
        return [i + 1 for i, num in enumerate(nums) if num > 0]
