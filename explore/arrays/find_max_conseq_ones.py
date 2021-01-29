# https://leetcode.com/explore/learn/card/fun-with-arrays/521/introduction/3238/

class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        num_ones = 0
        max_num_ones = 0
        in_ones = False
        
        for num in nums:
            if num == 1:
                if not in_ones:
                    num_ones = 1
                    in_ones = True
                else:
                    num_ones += 1
            #if num == 0:
            else:
                if in_ones:
                    in_ones = False
                    if num_ones > max_num_ones:
                        max_num_ones = num_ones
                        
        # in case the run did not stop
        if num_ones > max_num_ones:
            max_num_ones = num_ones
                        
        return max_num_ones
                    

        