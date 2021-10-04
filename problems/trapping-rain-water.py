# https://leetcode.com/problems/trapping-rain-water

class Solution:
    def trap_arrays(self, height: List[int]) -> int:
        # Approach, array based
        # for each position, the water is:
        # min(maxleft, maxright) - height
        
        # find maxleft and maxright
        maxleft = [0 for _ in range(len(height))]  # max height on left from current index
        maxright = [0 for _ in range(len(height))]
        N = len(height)
        
        for i in range(len(height)):
            if i == 0:
                maxleft[0] = 0
                maxright[N - 1] = 0
            else:
                maxleft[i] = max(maxleft[i-1], height[i-1])
                maxright[N-i-1] = max(maxright[N-i], height[N-i])
                
        water = 0
        for i, h in enumerate(height):
            # water in this column
            water += max(0, min(maxleft[i], maxright[i]) - h)
            
        return water
                
        
    def trap(self, height: List[int]) -> int:
        # Approach: 2 pointers
        # Process column by column
        left, right = 0, len(height) - 1
        
        leftmax = rightmax = water = 0
        
        while left < right:
            if height[left] <= height[right]:
                # slopes to left
                leftmax = max(leftmax, height[left])
                water += leftmax - height[left]
                left += 1
                
            else:
                # slopes ro right
                rightmax = max(rightmax, height[right])
                water += rightmax - height[right]
                right -= 1
    
        return water
        