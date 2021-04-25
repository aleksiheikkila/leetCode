# https://leetcode.com/explore/learn/card/binary-search/125/template-i/951/

# The guess API is already defined for you.
# @param num, your guess
# @return -1 if my number is lower, 1 if my number is higher, otherwise return 0
# def guess(num: int) -> int:

class Solution:
    def guessNumber(self, n: int) -> int:
        left, right = 1, n
        
        while left <= right:
            mid = (left + right) // 2
            
            resp = guess(mid)
            if resp == 0:
                return mid
            elif resp < 0:
                # number I picked is lower than your guess 
                right = mid - 1
            else:
                left = mid + 1
                
        raise RuntimeError("No solution")
            