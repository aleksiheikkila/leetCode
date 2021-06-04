# https://leetcode.com/problems/longer-contiguous-segments-of-ones-than-zeros/

class Solution:
    
    def checkZeroOnes(self, s: str) -> bool:
        curr_zeros, curr_ones, best_zeros, best_ones = 0, 0, 0, 0
        
        for c in s:
            if c == "0":
                curr_zeros += 1
                curr_ones = 0
            else:
                curr_zeros = 0
                curr_ones += 1
                
            best_zeros = max(best_zeros, curr_zeros)
            best_ones  = max(best_ones, curr_ones)
            
        return best_ones > best_zeros
            
            
        
    def checkZeroOnes_old(self, s: str) -> bool:
        lengths = {"0": 0,
                   "1": 0}
        
        digit_on = None
        curr_streak = -1
        
        for digit in s:
            if digit != digit_on or digit_on is None:
                if digit_on is not None:
                    lengths[digit_on] = max(curr_streak, lengths[digit_on])
                curr_streak = 1
                digit_on = digit
            else:
                curr_streak += 1
                
        lengths[digit_on] = max(curr_streak, lengths[digit_on])
        
        return lengths["1"] > lengths["0"]
        
                
        