# https://leetcode.com/problems/how-many-numbers-are-smaller-than-the-current-number

class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        
        count_smaller_nums = {}
        for idx, num in enumerate(sorted(nums)):
            # take only based on the first occurence
            if num not in count_smaller_nums:
                count_smaller_nums[num] = idx
        
        rst = []
        for num in nums:
            rst.append(count_smaller_nums[num])
            
        return rst
