# https://leetcode.com/problems/shifting-letters


def shift(char: str, n: int, alphabet_size: int = 26) -> str:
    n = n % alphabet_size
    new_ord = ord(char) + n
    if new_ord > 122:
        new_ord = 96 + (new_ord - 122)
    
    return chr(new_ord)
        

class Solution:
    def shiftingLetters(self, s: str, shifts: List[int]) -> str:
        shifted_chars = []
        needed_shifts = []
        cum = 0
        for num_shifts in shifts[::-1]:
            cum += num_shifts
            needed_shifts.append(cum)
            
        needed_shifts.reverse()
        
        # make shifts
        for i in range(len(needed_shifts)):
            shifted_chars.append(shift(char = s[i], n = needed_shifts[i]))

        return "".join(shifted_chars)
        