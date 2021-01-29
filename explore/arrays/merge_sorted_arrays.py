# https://leetcode.com/explore/learn/card/fun-with-arrays/525/inserting-items-into-an-array/3253/

class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        pos1 = m - 1
        pos2 = n - 1
        
        for pos in range(m + n - 1, -1, -1):
            if pos1 < 0:
                nums1[pos] = nums2[pos2]
                pos2 -= 1
            elif pos2 < 0:
                nums1[pos] = nums1[pos1]
                pos1 -= 1
            elif nums1[pos1] >= nums2[pos2]:
                nums1[pos] = nums1[pos1]
                pos1 -= 1
            else:
                nums1[pos] = nums2[pos2]
                pos2 -= 1
