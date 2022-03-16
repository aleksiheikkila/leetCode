# https://leetcode.com/explore/challenge/card/april-leetcoding-challenge-2021/596/week-4-april-22nd-april-28th/3718/

class Solution:
    def countBinarySubstrings(self, s: str) -> int:
        """
        count the number of contiguous zeros / ones (that's a block)
        When the binary digit changes (block ends), the number is substrs is incremented 
        by the min of prev and current block length)
        """
        
        curr_block_bit = s[0]
        curr_block_len, prev_block_len = 0, 0
        num_binary_substrs = 0
        
        for bit in s:
            if bit == curr_block_bit:
                # block continues
                curr_block_len += 1
            else:
                # block ends, add to answer and reset
                num_binary_substrs += min(curr_block_len, prev_block_len)
                prev_block_len = curr_block_len
                curr_block_bit = bit
                curr_block_len = 1
                  
        num_binary_substrs += min(curr_block_len, prev_block_len)    
        
        return num_binary_substrs
    