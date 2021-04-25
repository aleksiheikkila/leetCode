# https://leetcode.com/problems/maximum-subarray/submissions/
class Solution:
    
    def maxSubArray2(self, nums: List[int]) -> int:
        """ Kadane's algo """
        global_max, curr_max = float("-inf"), 0
        
        for n in nums:
            curr_max = max(n, curr_max + n)  # start new block or continue?
            if curr_max > global_max:
                global_max = curr_max
                
        return global_max
        
        
    def maxSubArray(self, nums: List[int]) -> int:
        """Divide and conquer solution"""
        def div_and_conq(nums, i, j):
            # i is the starting index. j is the "one past" index...
            
            # Returns 
            # a: max contig sum in nums[i:j] that includes 1st val (Starts from the beginning)
            # m: max contig sum anywhere in nums[i:j]
            # b: max contig sum anywhere in nums[i:j] that includes last val j-1
            # s: total sum on vals in nums[i:j]
            
            if i == j - 1:
                # case with just one value...
                return nums[i], nums[i], nums[i], nums[i]
            
            # midpoint
            mid = (i + j) // 2
            
            # compute for left half
            a1, m1, b1, s1 = div_and_conq(nums, i, mid)
            
            # compute for right half
            a2, m2, b2, s2 = div_and_conq(nums, mid, j)
            
            # Combine a, m, b, s values from left and right halves 
            # to form a, m, b, s for whole array (bottom up)
            
            a = max(a1, s1 + a2)
            m = max(m1, m2, b1 + a2)
            b = max(b2, b1 + s2)
            s = s1 + s2
            
            return a, m, b, s
        
        
        _, m, _, _ = div_and_conq(nums, 0, len(nums)) 
        return m
    