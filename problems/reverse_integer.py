class Solution:
    # 32 bit signed integer goes from -2147483648 (-2**31) to 2147483647 (2**31 - 1)
    def reverse(self, x: int) -> int:
        # faster than 85%, less than 22 mem
        reversed_wo_sign = int(str(abs(x))[::-1])
        if x < 0:
            return -reversed_wo_sign if reversed_wo_sign < 2**31 else 0
        else:
            return reversed_wo_sign if reversed_wo_sign < 2**31 - 1 else 0
            
            
    def reverse2(self, x: int) -> int:      
        sign = -1 if x < 0 else 1
        x *= sign
        rev = 0
        
        while x > 0:
            x, last_digit = divmod(x, 10)
            rev = 10*rev + last_digit
            
        if sign*rev < -(2**31) - 1 or sign*rev > 2**31:
            return 0
            
        return sign * rev
        
        