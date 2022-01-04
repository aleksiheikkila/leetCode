# https://leetcode.com/problems/word-break-ii/
# HARD

"""
Check word-break.py for more explanation.

Here I will use that as a template and just add the bookkeeping to retain
all possible word combinations.

Getting the word combinations is slower that figuring out if these is solution(s) or not.
So I added the code from word-break.py as a function canWordBreak to check that first.
We can then terminate early if no solutions is to be found.

"""

from collections import defaultdict


class Solution:
    def canWordBreak(self, s: str, wordDict: List[str]) -> bool:
        max_word_len = max(len(w) for w in wordDict)
        words_set = set(wordDict)
        
        breakable = [1] + [0 for _ in range(len(s))]
        # we could extend the "max_word_len" optimization to make breakable smaller...
        
        for curr_idx in range(1, len(breakable)):
            for prev_idx in range(max(0, curr_idx - max_word_len), curr_idx):
                if not breakable[prev_idx]:
                    continue
                word = s[prev_idx:curr_idx]
                if word in words_set:
                    breakable[curr_idx] = 1
                    break
        
        return breakable[-1]  # integer as bool


    def wordBreak(self, s: str, wordDict: List[str]) -> bool:

        # first check is solution exists:
        if not self.canWordBreak(s, wordDict):
            return []

        # then find the solution
        max_word_len = max(len(w) for w in wordDict)
        words_set = set(wordDict)
        
        N = len(s)
        breakable = defaultdict(list)
        breakable[0].append("")
        # we could extend the "max_word_len" optimization to make breakable smaller...
        
        for curr_idx in range(1, N+1):
            # remove the parts of breakable no longer needed (save some memory)
            if curr_idx - max_word_len - 1 >= 0:
                del breakable[curr_idx - max_word_len - 1]

            for prev_idx in range(max(0, curr_idx - max_word_len), curr_idx):
                if not breakable[prev_idx]:
                    continue
                word = s[prev_idx:curr_idx]
                if word in words_set:
                    breakable[curr_idx].extend([w + " " + word if w != "" else word
                                                for w in breakable[prev_idx]])
        
        return breakable[N]
        