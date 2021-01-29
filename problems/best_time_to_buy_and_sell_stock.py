class Solution:  
    def maxProfit(self, prices: List[int]) -> int:
        best_profit = 0  # running max
        
        for day_num, price in enumerate(prices):
            if day_num == 0:
                buy_price = price
                sell_price = 0
                continue
                
            if price < buy_price:
                # better entry, reset
                buy_price = price
                sell_price = 0
                #best_profit = max(sell_price - buy_price, best_profit)
            elif price > sell_price:
                # better exit, update best profit
                sell_price = price
                best_profit = max(sell_price - buy_price, best_profit)
            
        return best_profit
            
            