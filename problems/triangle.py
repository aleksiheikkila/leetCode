# https://leetcode.com/explore/challenge/card/april-leetcoding-challenge-2021/595/week-3-april-15th-april-21st/3715/

class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        # start from bottom, determine minimum sum to the end from each pos
        
        minsums = [v for v in triangle[-1]]  # last row
        for row in triangle[-2::-1]:  # from the second last to the first
            for i, v in enumerate(row):
                minsums[i] = v + min(minsums[i:i+2])
                   
        return minsums[0]
              