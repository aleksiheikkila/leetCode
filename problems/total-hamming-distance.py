# https://leetcode.com/problems/total-hamming-distance

class Solution:
    
    def totalHammingDistance(self, nums: List[int]) -> int:
        # Determine total Hamming distance for every bit position, then sum these
        #         
        # count of zeros and ones for every bit position
        bitcounts = [[0, 0] for _ in range(30)]  # 30 bits needed for the given range
        
        for n in nums:
            for bitcount in bitcounts:
                bitcount[n & 1] += 1  # is this bit one or zero?
                n >>= 1  # move to the next bit

        # for every bit position, the difference is zeros*ones (all possible pairs)        
        return sum(zeros*ones for zeros, ones in bitcounts)
        
        
      
    # TOO SLOW:
    def totalHammingDistance_slow(self, nums: List[int]) -> int:
        # OLD, too slow. NOT ACCEPTED
        memo = {}  # tuple of (lower, higher) -> dist
        total_dist = 0
        numz = sorted(nums)
        
        for i in range(len(numz)):
            for j in range(i+1, len(numz)):
                if (numz[i], numz[j]) not in memo:
                    memo[numz[i], numz[j]] = self._hammingDistance(numz[i], numz[j])
                total_dist += memo[(numz[i], numz[j])]
               
        return total_dist

    def _hammingDistance(self, x: int, y: int) -> int:
        dist = 0
        while x > 0 or y > 0:
            x, modx = divmod(x, 2)
            y, mody = divmod(y, 2)
            if modx != mody:
                dist += 1
        
        return dist
    
    
        