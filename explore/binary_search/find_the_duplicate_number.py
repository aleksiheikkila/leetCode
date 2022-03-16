# https://leetcode.com/explore/learn/card/binary-search/146/more-practices-ii/1039/

class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        n = sorted(nums)
        left, right = 0, len(n) - 1
        
        while left < right:
            mid = left + (right - left) // 2
            
            if n[mid] <= mid:
                right = mid
            else:
                left = mid + 1
                
        return n[mid]
    