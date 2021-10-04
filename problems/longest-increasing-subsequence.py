# https://leetcode.com/problems/longest-increasing-subsequence

class Solution:
    # A subsequence is a seq that can be derived from an array 
    # by deleting some or no elements wo changing the order of the remaining elems.
    def lengthOfLIS_O_n2(self, nums: List[int]) -> int:
        # runtime O(n^2)... there is a nlogn solution as well
        N = len(nums)
        dp = [1] * N  # LIS up to this index
        
        for i in range(1, N):
            for j in range(i):
                if nums[j] < nums[i]:
                    dp[i] = max(dp[i], dp[j] + 1)
                
        return max(dp)
    
    def lengthOfLIS(self, nums: List[int]) -> int:
        # runtime O(n*log(n))... 
        # with binary search
        seq = []  # keep this in sorted order
        
        for num in nums:
            idx = bisect_left(seq, num)  
            
            if idx < len(seq):
                seq[idx] = num
            else:
                seq.append(num)
        
        return len(seq)