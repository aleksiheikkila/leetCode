# https://leetcode.com/problems/permutation-sequence
# HARD

# 


from math import factorial

class Solution:
    def getPermutation(self, n: int, k: int) -> str:
        
        rst = []
        k -= 1
        digits = [str(i) for i in range(1, n+1)]
        
        while n:
            """Infer in which group the kth one is"""
            group_size = factorial(n-1)  
            # ... if we select a number of the curr pos, there are (n-1)! alternatives for that
            # so thats gonna be the group size
            
            # in which group the kth one is?
            kth_in_group_idx = k // group_size
            
            # ok, based on that, get the next digit for the result and decrease k
            rst.append(digits.pop(kth_in_group_idx))
            k -= (kth_in_group_idx * group_size)

            # move to next digit
            n -= 1
            
        return "".join(rst)
        