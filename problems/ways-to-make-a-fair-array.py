# https://leetcode.com/problems/ways-to-make-a-fair-array

class Solution:
    def waysToMakeFair(self, nums: List[int]) -> int:
        # array is fair if the sum of the odd-indexed values equals the sum of the even-indexed values    
        
        # Sketching:
        # [2,1,6,4]:
        
        # odds 8, evens 5
        # at idx 0:
        # left: odds: 0, evens: 0
        # right (incl): 8 / 4
        
        # at idx 1:
        # left: 2 / 0
        # right 6 / 4
        
        ways = 0
        
        # find total sum of even, odd indexed
        tot_odd, tot_even = 0, 0
        for i, num in enumerate(nums):
            if i % 2 == 0:
                tot_even += num
            else:
                tot_odd += num
                       
        left_odd, left_even = 0, 0
        right_odd, right_even = tot_odd, tot_even
        
        for i, num in enumerate(nums):
            if i % 2 == 0:
                right_even -= num
            else:
                right_odd -= num

            # when doing this comparison, left does not include the current element, and neither does right    
            # right_odd will become even after removing from element before that rigth subsection
            if (left_odd + right_even) == (left_even + right_odd):  
                ways += 1
            
            # then add the current num to corresponding left sum
            if i % 2 == 0:
                left_even += num
            else:
                left_odd += num

        return ways 
