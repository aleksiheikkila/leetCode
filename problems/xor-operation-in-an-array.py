# https://leetcode.com/problems/xor-operation-in-an-array

class Solution:
    def xorOperation(self, n: int, start: int) -> int:
        rst = 0  # XOR with zero is the other value itself
        for i in range(n):
            rst ^= start + 2*i
        
        return rst
        
        
        