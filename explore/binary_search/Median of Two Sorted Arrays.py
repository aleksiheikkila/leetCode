# https://leetcode.com/explore/learn/card/binary-search/146/more-practices-ii/1040/

# Naive
class Solution:
    def findMedianSortedArrays_v1(self, nums1: List[int], nums2: List[int]) -> float:
        n = len(nums1) + len(nums2)
        p1, p2, processed = 0, 0, 0
        v1, v2 = None, None  # last value, and the value before the last

        while processed <= n // 2:
            v2 = v1
            if p1 >= len(nums1):
                v1 = nums2[p2]
                p2 += 1  
            elif p2 >= len(nums2):
                v1 = nums1[p1]
                p1 += 1
            else:
                if nums1[p1] <= nums2[p2]:
                    v1 = nums1[p1]
                    p1 += 1
                else:
                    v1 = nums2[p2]
                    p2 += 1
            
            processed += 1
            
        if n % 2 == 0:
            # take mean
            return (v1 + v2) / 2
        else:
            # take the middle value
            return v1



    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        n = len(nums1) + len(nums2)        

        if len(nums1) <= len(nums2):
            shorter, longer = nums1, nums2
        else:
            shorter, longer = nums2, nums1

 

        # how many values to incl from shorter array
        left, right = 0, min(n//2, len(shorter) - 1)

        while left <= right:
            mid = (left + right) // 2
            nbr_vals_from_longer = (n // 2) - mid

            # then the different scenarios


            if shorter[mid]  


