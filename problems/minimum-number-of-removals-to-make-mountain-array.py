# https://leetcode.com/problems/minimum-number-of-removals-to-make-mountain-array

class Solution:
    def minimumMountainRemovals(self, nums: List[int]) -> int:
        def LIS(nums):
            # Now return the dp, which has LISes up to the array index...
            seq = []
            dp = []
            for num in nums:
                idx = bisect_left(seq, num)
                if idx < len(seq):
                    seq[idx] = num
                else:
                    seq.append(num)
                dp.append(len(seq))  # LIS up to this index...
            return dp
        

        _max = 0
        
        N = len(nums)
        dp_left = LIS(nums)
        dp_right = LIS(nums[::-1])  # increasing in reverse order, so decreasing in normal order
        #dp_right = dp_right[::-1]
        
        # Consider all possible mountain peak positions i:
        for i in range(1, N-1):
            if dp_left[i] > 1 and dp_right[N-1-i] > 1:  # must have valid ascent and descent before/after peak
                _max = max(_max, dp_left[i] + dp_right[N-1-i] - 1)
                # the minus one thing? dp_left and dp_right both include the index i... So that is counted twice
                
        return N - _max