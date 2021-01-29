# https://leetcode.com/problems/multiply-strings

class Solution:
    # Slower... Product, digit by digit
    def multiply2(self, num1: str, num2: str) -> str:
        prod = 0
        for exp1, c1 in enumerate(num1[::-1]):
            for exp2, c2 in enumerate(num2[::-1]):
                digit1 = int(c1)
                digit2 = int(c2)
                prod += digit1*10**exp1 * digit2*10**exp2
                
        return str(prod)
    
    
    # Way faster:
    def multiply(self, num1: str, num2: str) -> str:
        def str2int(s):
            # "indirect" conversion to int
            rst = 0
            for c in s:
                rst = 10*rst + ord(c) - ord("0")
            
            return rst
                
        return str(str2int(num1) * str2int(num2))
        
        
            