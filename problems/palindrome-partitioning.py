""" 131. Palindrome Partitioning. MEDIUM
https://leetcode.com/problems/palindrome-partitioning

Given a string s, partition s such that every substring of the partition is a palindrome. 
Return all possible palindrome partitioning of s.

A palindrome string is a string that reads the same backward as forward.

#####################

Approach:

Brute-forcing with dfs backtracking. 

For the reimaining part of the string, find palindromes and continue in dfs manner.
If we reach the end with just palindromes as partitions, add to result.
Backtrack

"""

class Solution:
    def is_palindrome(self, s: str, 
                      left_idx: int, right_idx: int) -> bool:
        """Helper to check is if s[left_idx:right_idx+1] is a palindrome"""
        
        while left_idx < right_idx:
            if s[left_idx] != s[right_idx]:
                return False
            left_idx += 1
            right_idx -= 1
        return True
    
    
    def partition(self, s: str) -> List[List[str]]:
        N = len(s)
        partitions = []
        result = []
        
        def dfs(i: int) -> None:
            # base case
            if i >= N:
                # okay, we have a valid partitioning
                result.append(partitions.copy())
                return
            
            # for the rest of the string, find palindromes
            for j in range(i, N):
                if self.is_palindrome(s, i, j):
                    partitions.append(s[i:j+1])
                    dfs(j+1)
                    partitions.pop()  # backtrack

        # launch dfs:            
        dfs(0)
        
        return result
        