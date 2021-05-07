# https://leetcode.com/problems/container-with-most-water/

class Solution:
    def maxArea(self, height: List[int]) -> int:
        left_idx, right_idx = 0, len(height) - 1 
        left, right = height[left_idx], height[right_idx]
        max_area = min(left, right) * right_idx
        
        while left_idx < right_idx:
            if left <= right:
                left_idx += 1
                if height[left_idx] > left:
                    new_area = min(height[left_idx], height[right_idx]) \
                                    * (right_idx - left_idx)
                    if new_area > max_area:
                        max_area = new_area
                    left = height[left_idx]
            
            else:
                right_idx -= 1
                if height[right_idx] > right:
                    new_area = min(height[left_idx], height[right_idx]) \
                                    * (right_idx - left_idx)
                    if new_area > max_area:
                        max_area = new_area
                    right = height[right_idx]
                
        return max_area
        