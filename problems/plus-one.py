# https://leetcode.com/problems/plus-one

class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        d = digits.copy()
        
        for i in reversed(range(len(d))):
            if d[i] == 9:
                # carry over
                continue
            else:
                d[i] += 1
                # if we have been carrying digits over to more significant bits:
                for j in range(i+1, len(d)):
                    d[j] = 0
                return d

        # case we had e.g. [9, 9, 9] --> [1, 0, 0, 0]    
        return [1] + [0] * len(d)