# https://leetcode.com/explore/learn/card/fun-with-arrays/511/in-place-operations/3260/

class Solution:
    def sortArrayByParity(self, A: List[int]) -> List[int]:
        # two pointers. One starting from both ends
        if len(A) < 2:
            return A
        
        p1 = 0
        p2 = len(A) - 1
        
        while p1 < p2:
            if A[p1] % 2 == 0:
                p1 += 1
                continue
            if A[p2] % 2 == 1:
                p2 -= 1
                continue
                 
            # now do a swap and proceed
            A[p1], A[p2] = A[p2], A[p1]
            p1 += 1
            p2 -= 1
            
        return A
