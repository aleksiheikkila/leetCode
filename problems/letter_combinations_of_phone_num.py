# https://leetcode.com/problems/letter-combinations-of-a-phone-number/

import itertools as it

class Solution:
    def __init__(self):
        self.digit_to_chars = {"2": "abc",
                             "3": "def",
                             "4": "ghi",
                             "5": "jkl",
                             "6": "mno",
                             "7": "pqrs",
                             "8": "tuv",
                             "9": "wxyz"
                             }
        
    def letterCombinations_itertools(self, digits: str) -> List[str]:
        if len(digits) == 0:
            return []
        
        charsets = [self.digit_to_chars[digit] for digit in digits]        
        return ["".join(comb) for comb in it.product(*charsets)]
            
        
        
    def letterCombinations(self, digits: str) -> List[str]:
        if len(digits) == 0:
            return []
        
        solution = []  # "passed by reference"
        self.letter_prod_helper(digits, "", solution)
        # what this needs to do is:
        # recursively dive the tree all the way to each leaf node, then add that to the sol
        # depth first

        return solution
        

    def letter_prod_helper(self, digits, currStr, solution):
        # Base case / Stop condition: exhausted the digits, at a leaf node
        if len(digits) == 0:
            solution.append(currStr)
            return  # back one level up

        for char in self.digit_to_chars[digits[0]]:
            # Recurse
            currStr = currStr + char
            self.letter_prod_helper(digits[1:], currStr, solution)
            # then remove the last char before going back one level up
            currStr = currStr[:-1]
 