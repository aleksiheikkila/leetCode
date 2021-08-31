# https://leetcode.com/problems/bitwise-and-of-numbers-range

class Solution:

    def rangeBitwiseAnd(self, left: int, right: int) -> int:
        # Observe:
        # if for any position a bit flips, that bit position will be zero in the rst
        # and all of the bit positions to the right of that will also be flipping and be zero
        
        # GOing upwards in numbers:
        # Whenever we add a new bit needed represent it, that bit and all bits to the right will be zero in the result
        # all the bits to the right were ones, then when we take the new MSB, those will turn to 0, ie flip.
        
        # Approach. Find how many consecutive common bits there are on the left side (MSBs)
        # And how many of the LSBs are flipping
        #
        
        num_shifts = 0
        # find the common part on the left side (MSBs)
        while left != right:
            # get rid of the LSB
            left = left >> 1
            right = right >> 1
            num_shifts += 1
            
        # when this finishes, left/right has the MSB common bits
        # The LSB bits will be zero
        # We achieve this my leftshifting num_shifts times (to add zeros to the right)
        return left << num_shifts
        