# https://leetcode.com/explore/learn/card/binary-search/137/conclusion/978/

# Perfect square?
# A perfect square is a number that can be expressed as 
# the square of a number from the same number system
# E.g. 5*5 = 25, so 25 is a perfect square

class Solution:
    def isPerfectSquare2(self, num: int) -> bool:
        from math import sqrt

        return sqrt(num) == int(sqrt(num))  # is this safe way to do it?
    
    def isPerfectSquare(self, num: int) -> bool:
        # with binary search
        left, right = 1, num

        while left <= right:
            mid = left + (right - left) // 2

            mid_squared = mid ** 2
            if mid_squared == num:
                return True
            elif mid_squared < num:
                # go to the right half
                left = mid + 1
            else:
                right = mid - 1

        return False
