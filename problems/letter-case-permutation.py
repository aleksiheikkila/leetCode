# https://leetcode.com/problems/letter-case-permutation

from typing import List
class Solution:
    def letterCasePermutation(self, s: str) -> List[str]:
        return self.letterCasePermute(s)
    
    def letterCasePermute(self, s: str) -> List[str]:
        """Recursive"""
        rst = []
        
        # Base cases
        if len(s) == 1:
            if not s[0].isalpha():
                rst.append(s[0])
            else:
                rst.append(s[0].upper())
                rst.append(s[0].lower())
            return rst
        
        if len(s) == 0:
            return []
        
        # Recurse case
        if not s[0].isalpha():
            rst.extend([s[0] + txt for txt in \
                        self.letterCasePermute(s[1:])])
        else:
            tmp = self.letterCasePermute(s[1:])
            rst.extend([s[0].upper() + txt for txt in tmp])
            rst.extend([s[0].lower() + txt for txt in tmp])
            
        return rst       
        