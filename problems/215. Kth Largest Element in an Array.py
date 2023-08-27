"""
https://leetcode.com/problems/kth-largest-element-in-an-array/
Medium

Min heap

Given an integer array nums and an integer k, return the kth largest element in the array.

Note that it is the kth largest element in the sorted order, not the kth distinct element.
"""

import heapq

class Solution:

    def findKthLargest_sort(self, nums: List[int], k: int) -> int:
        nums.sort()
        return nums[-k]

    # min heap solution
    def findKthLargest_heap(self, nums: List[int], k: int) -> int:
        """O(N log k)"""
        heap = []
        
        for num in nums:
            heapq.heappush(heap, num)
            
            if len(heap) > k:
                # O(log k)
                heapq.heappop(heap)
                
        return heap[0]
        
    # Quick select is better on average time complexity: O(N)
    # Worst case O(N^2)
    def findKthLargest(self, nums: List[int], k: int) -> int:
        """quickselect. This has the best average runtime complexity, but the leetcode inputs does not do this justice"""
        kth_largest_idx = len(nums) - k
        
        def quickselect(l: int, r: int):
            # select always the rightmost value as the pivot
            pivot = nums[r]
            p = l  # this is the index where we insert values less than or equal to the pivot
            
            for i in range(l, r):
                if nums[i] <= pivot:
                    # swap
                    nums[p], nums[i] = nums[i], nums[p]
                    p += 1
            # finally swap pivot to p index (pivot is nums[r])
            # pivot value is in its right place (left and right sides are not sorted)
            nums[p], nums[r] = nums[r], nums[p]
            
            # did we find the solution? or which half to study more?
            if p == kth_largest_idx:
                # pivot is the kth largest value
                return nums[p]
            elif p > kth_largest_idx:
                # search left side
                return quickselect(l, p - 1)
            else:
                return quickselect(p + 1, r)
            
        return quickselect(0, len(nums) - 1)
        