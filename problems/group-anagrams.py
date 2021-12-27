# https://leetcode.com/problems/group-anagrams
# Medium

# Hash table

from collections import defaultdict
from typing import List


class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagrams = defaultdict(list)
        # version 1: key: sorted string, value is a list of the anagrams seen
        # version 2: key: tuple of word counts. lowercase english letters
        # version 1 turned out to be faster with the inputs given 
        # (...but one could try v2 without extra function calls)
        
        def get_charcounts(str_: str) -> tuple:
            """(For version 2) Converts str_ to a tuple of charcounts
            First elements is the number of a's, 2nd b's etc.
            This is used for hashing (as dict keys)
            """
            counts = [0 for _ in range(26)]
            ord_a = ord('a')
            for char in str_:
                counts[ord(char) - ord_a] += 1
                
            return tuple(counts)
            
        
        for str_ in strs:
            # version 1:
            anagrams[str(sorted(str_))].append(str_)
            
            # version 2:
            #anagrams[get_charcounts(str_)].append(str_)
        
        return list(anagrams.values())
        