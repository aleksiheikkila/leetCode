# https://leetcode.com/problems/evaluate-reverse-polish-notation

from typing import List

class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        s = []
        
        for t in tokens:       
            if t.lstrip("-").isdigit():
                s.append(int(t))
            else:
                # is operator
                v1 = s.pop()
                v2 = s.pop()
                
                if t == "+":
                    s.append(v1 + v2)
                elif t == "-":
                    s.append(v2 - v1)
                elif t == "*":
                    s.append(v1 * v2)
                elif t == "/":
                    s.append(int(v2 / v1))
                else:
                    raise ValueError(f"Unknown token {t}")
                
        return s[-1]
    