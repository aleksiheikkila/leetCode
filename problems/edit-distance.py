# https://leetcode.com/problems/edit-distance

"""
Dynamic programming

let
f(i,j) = minimum edit distance between word1[:i] and word2[:j]  (i,j not included)
f(len(word1) = N1, len(word2) = N2) is what we need

Relation:
f(i,j) = minimum of the following:
    f(i-1, j) + 1    # rem last from w1
    f(i, j-1) + 1    # insert to the end of w1 the char in w2
    f(i-1, j-1)      # if word1[i] == word2[j]
    f(i-1, j-1) + 1  # if word1[i] != word2[j]  ie replacement
    
Base case:
f(i,j) = max(i, j) if i == 0 or j == 0  # as we need i or j deletions or inserts

I will retain two consequent rows of the dp matrix (no need to persist it all)

"""


class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        N2 = len(word2)
        
        # first row, i=0, so col values are j as per the base case
        dp = list(range(N2 + 1))
        # use two rows of the matrix, dp is the previous and new_dp is the next one
        
        for r, chr1 in enumerate(word1, 1):
            new_dp = [r] + [0] * N2
            for c, chr2 in enumerate(word2, 1):
                new_dp[c] = min(
                                dp[c] + 1,  # dp is the previous row, i-1
                                new_dp[c-1] + 1,  # new_dp is the current row i
                                dp[c-1] + int(chr1 != chr2)  # handles last two options
                            )
            dp = new_dp
        
        # return the last cell value
        return dp[-1]
