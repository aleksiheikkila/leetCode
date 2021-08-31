# https://leetcode.com/problems/3sum-closest/

class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        # with a sorted array and three pointers
        result = None
        min_diff = float("inf")
        
        nums.sort()
        
        for i in range(len(nums) - 2):  # 'current' pointer:           
            left = i + 1
            right = len(nums) - 1
            
            while left < right:
                curr_sum = nums[i] + nums[left] + nums[right]
                
                if curr_sum == target:
                    # smallest diff possible so terminate
                    return curr_sum
                
                diff = abs(curr_sum - target)

                if diff < min_diff:
                    min_diff = diff
                    result = curr_sum
                    
                if curr_sum < target:
                    # increase left
                    left += 1
                else:
                    # current sum larger than target, decrease right
                    right -= 1

        return result
