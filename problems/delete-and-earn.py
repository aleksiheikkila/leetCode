# https://leetcode.com/problems/delete-and-earn

class Solution:
    def deleteAndEarn(self, nums: List[int]) -> int:
        from collections import Counter
            
        counts = Counter(nums)
        
        prev = None
        avoid = using = 0  # score if we avoid using, or if we use
        
        for num in sorted(counts):
            if prev != num - 1:
                # prev (next smaller num) is NOT adjacent to curr
                # Scoring "num" does not delete any values
                avoid = max(avoid, using)
                using = max(avoid, using) + num * counts[num]
            else:
                # adjacent (or first value)
                avoid, using = max(avoid, using), avoid + num * counts[num]
            prev = num
                
        return max(avoid, using)
                