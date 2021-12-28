# https://leetcode.com/problems/h-index
# Medium

"""
Given an array of integers citations where citations[i] is the number of citations 
a researcher received for their ith paper, return compute the researcher's h-index.

According to the definition of h-index on Wikipedia: A scientist has an index h if h of their 
n papers have at least h citations each, and the other n − h papers have no more than h citations each.

If there are several possible values for h, the maximum one is taken as the h-index.
"""

class Solution:
    def hIndex(self, citations: List[int]) -> int:
        # linear scan brute forcing, O(n)
        
        if len(citations) == 1:
            return min(citations[0], 1)
            
        for paper_num, cits in enumerate(reversed(sorted(citations)), start=1):
            if paper_num > cits:
                # Violation! OK, the previous one then!
                return paper_num - 1
        
        return paper_num