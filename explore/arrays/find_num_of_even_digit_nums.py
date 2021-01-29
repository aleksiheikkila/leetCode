# https://leetcode.com/explore/learn/card/fun-with-arrays/521/introduction/3237/

class Solution:
    from math import log10
    
    def findNumbers(self, nums: List[int]) -> int:
        # via strings:
        # return sum(len(str(num)) % 2 == 0 for num in nums)
        
        # without converting to strigns
        return sum((int(log10(num)) + 1) % 2 == 0 for num in nums)
