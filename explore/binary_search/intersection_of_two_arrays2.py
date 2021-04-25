# https://leetcode.com/explore/learn/card/binary-search/144/more-practices/1029/

class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        from collections import defaultdict
        
        c1, c2 = defaultdict(int), defaultdict(int)
        rst = []
        
        # counts
        for num in nums1:
            c1[num] += 1
        for num in nums2:
            c2[num] += 1
            
        # does this make a difference?
        if len(c1) < len(c2):
            for num, count in c1.items():
                if num in c2:
                    rst.extend([num] * min(count, c2[num]))
        else:
            for num, count in c2.items():
                if num in c1:
                    rst.extend([num] * min(count, c1[num]))
                    
        return rst
            