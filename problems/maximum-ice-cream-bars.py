# https://leetcode.com/problems/maximum-ice-cream-bars

class Solution:
    def maxIceCream(self, costs: List[int], coins: int) -> int:
        from collections import Counter
        
        rst = 0
        counts = Counter(costs)
        
        for unit_price in sorted(counts):
            if unit_price > coins:
                break
            
            num_to_buy = min(coins // unit_price, counts[unit_price])
            coins -= num_to_buy * unit_price
            rst += num_to_buy
            
        return rst
        
                
    def maxIceCream(self, A, coins):
        """Simple"""
        A.sort()
        for i, a in enumerate(A):
            coins -= a
            if coins < 0:
                return i
        return len(A)