# https://leetcode.com/explore/learn/card/binary-search/144/more-practices/1034/

# Not based on a binary search

class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        # this oneliner works fine:
        # return list(set(nums1).intersection(set(nums2)))
        # or just:
        return list(set(nums1) & set(nums2))
        
        set1, set2 = set(nums1), set(nums2)
        
        if len(set1) < len(set2):
            return [x for x in set1 if x in set2]
        else:
            return [x for x in set2 if x in set1]
        