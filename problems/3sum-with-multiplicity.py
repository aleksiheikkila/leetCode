# https://leetcode.com/problems/3sum-with-multiplicity

# Convoluted and slow solution...
# TODO: Improve

from collections import Counter
import math

class Solution:
    def threeSumMulti(self, arr: List[int], target: int) -> int:
        result = 0
        #counts = Counter(arr)
        #nums = sorted(counts.keys())
        
        arr.sort()
        
        def sum_to_num(num):
            assert num >= 1
            rst = 0
            
            while num > 0:
                rst += num
                num -= 1
            return rst
                
        
        #for curr in range(len(nums) - 2):
        for curr in range(len(arr) - 2):
            left, right = curr + 1, len(arr) - 1
            
            while left < right:

                curr_sum = arr[curr] + arr[left] + arr[right]
                
                if curr_sum == target:
                    leftcount, rightcount = 1, 1
                    
                    same_left_right = arr[left] == arr[right]
                    
                    while left < len(arr) - 1 and arr[left] == arr[left + 1]:
                        left += 1
                        leftcount += 1
                        
                    if same_left_right:
                        result += sum_to_num(leftcount - 1)
                        

                    while right > 0 and arr[right] == arr[right - 1]:
                        right -= 1
                        rightcount += 1
                        
                    if same_left_right:
                        result += sum_to_num(leftcount - 1)
                    else:

                        result += leftcount * rightcount
                        left += 1
                        right -= 1
                
                elif curr_sum < target:
                    left += 1
                    
                else:
                    right -= 1
        
        
        return result % (7 + 10**9)
        
        