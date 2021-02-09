# https://leetcode.com/explore/learn/card/fun-with-arrays/523/conclusion/3228/
# Relatively slow one-liner

class Solution:
    def heightChecker(self, heights: List[int]) -> int:        
        return sum(el1 != el2 for el1, el2 in zip(heights, sorted(heights)))
            