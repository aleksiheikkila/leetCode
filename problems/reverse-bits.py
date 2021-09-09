# https://leetcode.com/problems/reverse-bits

class Solution:
    def reverseBits(self, n: int) -> int:
        #reversed_str = format(n, '032b')[::-1]
        # need to format to keep the leading zeros...        
        #return int(reversed_str, 2)
        
        ans = 0
        
        for i in range(32):  # 32 bit ints
            bit = (n >> i) & 1  # select the next bit from right
            ans = (ans << 1) + bit  # add it to ans, to the right side
            
        return ans
        