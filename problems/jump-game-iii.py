# https://leetcode.com/problems/jump-game-iii

class Solution:
    def canReach(self, arr: List[int], start: int) -> bool:        
        """Can we reach any zero value"""
        if len(arr) == 0 or start < 0 or start >= len(arr):
            return False
        
        visited = set()  # already visited indices
        stack = [start]  # indices to be explored
        
        while stack:
            idx = stack.pop()
            visited.add(idx)
            num = arr[idx] 
            if num == 0:
                return True
            
            # Add possible new indices to explore
            if idx - num >= 0 and idx - num not in visited:
                stack.append(idx - num)
            if idx + num < len(arr) and idx + num not in visited:
                stack.append(idx + num)
                
        return False
                