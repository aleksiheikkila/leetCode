# https://leetcode.com/problems/product-of-array-except-self

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        answer = [1] * n
        
        # arrays a[i] containing the product of the values
        # to the left of i, and to right of i (i not included)
        prod_to_left = [1] * n
        prod_to_right = [1] * n
        
        for i in range(1, n):
            prod_to_left[i] = nums[i-1] * prod_to_left[i-1] 
            
        for i in range(n-2, -1, -1):
            prod_to_right[i] = nums[i+1] * prod_to_right[i+1] 
        
        for i in range(len(answer)):
            answer[i] = prod_to_left[i] * prod_to_right[i]
        
        return answer
