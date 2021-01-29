class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # this is actually the cumulative sum of price increases
        max_profit = 0
        
        for prev, curr in zip(prices[:-1], prices[1:]):
            if curr > prev:
                max_profit += curr - prev
                
        return max_profit
        
        
    def maxProfit2(self, prices: List[int]) -> int:
        # this is actually the cumulative sum of price increases
        max_profit = 0
        i = 0
        
        while len(prices) - i >= 2:
            if prices[i+1] - prices[i] > 0:
                max_profit += prices[i+1] - prices[i]
            i += 1
        
        return max_profit