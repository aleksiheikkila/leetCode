# https://leetcode.com/problems/string-to-integer-atoi

class Solution:
    def myAtoi(self, s: str) -> int:
        # The atoi() function converts a character string to an integer value.
        sign = 1
        left = 0

        # 1. skip preceding whitespace
        for c in s:
            if c == " ":
                left += 1
            else:
                break
                
        if left == len(s):
            return 0

        # 2. sign
        if s[left] in ("+", "-"):
            sign = -1 if s[left] == "-" else 1
            left += 1
        
        # 3. read digits until the end of string or nondigit char
        digits = []
        for c in s[left:]:
            if not c.isdigit():
                break
            else:
                digits.append(c)
        
        if len(digits) == 0:
            return 0
        
        int_part = int("".join(digits))
        if sign == -1 and int_part > 2**31:
            int_part = 2**31
        elif sign == 1 and int_part > 2**31 - 1:
            int_part = 2**31 - 1
            
        return sign * int_part
        