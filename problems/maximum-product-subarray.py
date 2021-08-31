# https://leetcode.com/problems/maximum-product-subarray

class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        # DP
        # keep track of the current minimum and maximum 
        # (both bc of negative numbers)
        # Edge case: zeros... this handles them too
        
        rst = nums[0]
        curMin, curMax = 1, 1  # one is the neutral val for prod
        
        for n in nums:
            # NOT NEEDED:
            #if n == 0:
            #    curMin, curMax = 1, 1
            #    continue
                
            curMax, curMin = max(curMax * n, curMin * n, n), \
                             min(curMax * n, curMin * n, n)

            rst = max(rst, curMax)       
            
        return rst
  