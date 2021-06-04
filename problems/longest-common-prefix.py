# https://leetcode.com/problems/longest-common-prefix

class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        min_len = min(len(s) for s in strs)
        if min_len == 0:
            return ""
         
        idx = 0
        while idx < min_len:
            if len(set([s[idx] for s in strs])) > 1:
                break
            idx += 1

        return strs[0][:idx]
    