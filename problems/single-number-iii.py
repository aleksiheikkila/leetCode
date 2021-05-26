# https://leetcode.com/problems/single-number-iii

from collections import defaultdict

class Solution:
    def singleNumber(self, nums: List[int]) -> List[int]:
        occurences = defaultdict(int)
        
        for num in nums:
            occurences[num] += 1
        
        rst = []
        for num, num_occ in occurences.items():
            if num_occ == 1:
                rst.append(num)
                if len(rst) == 2:
                    break
                
        return rst