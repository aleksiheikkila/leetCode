# https://leetcode.com/problems/counting-bits

class Solution:
    def countBits(self, num: int) -> List[int]:
        rst = []
        
        for n in range(num+1):
            rst.append(bin(n).count("1"))
            
        return rst


    def countBits2(self, num: int) -> List[int]:
        # this is probs more something they we after
        setbits = [0]

        for i in range(1, num+1):
            setbits.append(setbits[i >> 1] + (i & 1))
        # bitshift >> 1 == halve the number i (round down)
        # Example
        # i is 14 (0b1110)
        # i >> 1 = 7 (0b111)
        # Check the (already calculated) number of set bits in i >> 1 
        # and check whether the last bit of i is 1 or zero (zero in the examples case)

        return setbits

