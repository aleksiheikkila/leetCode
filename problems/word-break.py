# https://leetcode.com/problems/word-break/submissions/
# Medium

"""
Dynamic programming approach. Iterative.

Let:
breakable: list of len(s) + 1 of flags:
breakable[i] indicates whether s[:i] can be segmented into words in given dict, in any way.

Scan the input word s linearly.

When checking at character position i of s, 
do another loop over the previous locations (prev_idx) and for those of them that has
what comes before breakable, test if the dictionary contains the words s[prev_idx:i].
If so, we are breakable up to the current index.

Base case:
breakable[0] = 1,  can break empty string.

Optimizations:
max_word_len


breakable[len(s) + 1] = breakable[-1] is the answer:
1 = True, can break
0 = False, cannot

"""

class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
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
        