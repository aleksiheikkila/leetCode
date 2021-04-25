# https://leetcode.com/explore/learn/card/recursion-ii/470/divide-and-conquer/2944/

class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        # mergesort
        
        # base case
        if len(nums) <= 1:
            return nums
        
        pivot = len(nums) // 2
        sorted_left  = self.sortArray(nums[:pivot])
        sorted_right = self.sortArray(nums[pivot:])
        
        return merge(sorted_left, sorted_right)
        
        
    def merge(llist, rlist):
        merged = []
        lptr, rptr = 0, 0  # pointers

        while lptr < len(llist) and r_ptr < len(rlist):
            if llist[lptr] < rlist[rptr]:
                merged.append(llist[lptr])
                lptr += 1
            else:
                merged.append(rlist[rptr])
                rptr += 1

        # Then what is left in the lists
        # these lists are always sorted, so no need to check
        merged.extend(llist[lptr:])
        merged.extend(rlist[rptr:])

        return merged
        