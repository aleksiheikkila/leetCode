# https://leetcode.com/problems/find-minimum-in-rotated-sorted-array-ii

# O(log(N))
# the worst case, only duplicates, reduces to linear time O(N)
class Solution:
    def findMin(self, nums: List[int]) -> int:
        lo, hi = 0, len(nums) - 1
        
        while lo < hi:
            mid = (lo + hi) // 2
            if nums[mid] > nums[hi]:
                # pivot (and min) is in right side
                lo = mid + 1
            elif nums[mid] < nums[hi]:
                # min is in left, or at mid
                hi = mid
            else:
                # a tie, nums[mid] == nums[hi]
                # not known which subpart the min is in
                # just decrease hi by one, trying to break out that way
                hi -= 1
        
        # end criterion: lo == hi, and the min value is there
        return nums[lo]
        