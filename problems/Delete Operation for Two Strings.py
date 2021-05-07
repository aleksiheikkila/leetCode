# https://leetcode.com/explore/challenge/card/may-leetcoding-challenge-2021/598/week-1-may-1st-may-7th/3734/

class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        
        # Find longest common substring (LCS) for the two words.
        # The minDistance to make them same is: len(word1) + len(word2) - 2*LCS
        
        # DP problem
        m, n = len(word1), len(word2)
        dp = [[0] * (n+1) for _ in range(m+1)]  
        # empty strings have zero len common part
        # handle i-1 case by making dp of size m+1
        
        for i in range(1, m+1):
            for j in range(1, n+1):
                # i,j are 1-based, words are 0-based:
                if word1[i - 1] == word2[j - 1]:
                    dp[i][j] = 1 + dp[i - 1][j - 1]
                else:
                    dp[i][j] = max(dp[i][j - 1], dp[i - 1][j])  # which one is larger
                       
        return m + n - 2*dp[m][n]
