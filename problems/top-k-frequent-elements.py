# https://leetcode.com/problems/top-k-frequent-elements

from collections import Counter, defaultdict

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # bucket sort
        
        if k > len(nums):
            raise ValueError("k must be <= len(nums)")
        
        # frequency counts: O(N)
        counts = Counter(nums)
        
        # generate buckets: O(M) (M distinct freqs)
        buckets = defaultdict(set)
        for num, freq in counts.items():
            buckets[freq].add(num)
        
        # collect the top K
        topK = []
        # naively go from freq: len(nums) to 1 
        # O(M)?
        for freq in range(len(nums), 0, -1):
            if freq in buckets:
                topK.extend(buckets[freq])
                if len(topK) >= k:
                    break
        
        return topK[:k]
        