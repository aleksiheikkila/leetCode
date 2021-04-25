# https://leetcode.com/explore/learn/card/binary-search/135/template-iii/945/

class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        # find match to x, or where the x falls into
        
        left, right = 0, len(arr) - 1
        
        start_idx = 0  # Points to prev (smaller) value, if target x falls between to vals. Or to a matching val
        rst = []
        
        while left <= right:
            mid = (left + right) // 2
            
            if arr[mid] == x:
                start_idx = mid
                break
            if arr[mid] < x:
                start_idx = mid
                left = mid + 1
            else:
                right = mid - 1
                
        #print("Start idx:", start_idx)
        lo, hi = start_idx, start_idx + 1
        
        for _ in range(k):
            if lo < 0:
                rst.append(arr[hi])
                hi += 1
                continue
            if hi >= len(arr):
                rst.append(arr[lo])
                lo -= 1
                continue
            
            if abs(arr[lo] - x) < abs(arr[hi] - x):
                rst.append(arr[lo])
                lo -= 1
            elif abs(arr[lo] - x) > abs(arr[hi] - x):
                rst.append(arr[hi])
                hi += 1
            else:
                if arr[lo] < arr[hi]:
                    rst.append(arr[lo])
                    lo -= 1
                else:
                    rst.append(arr[hi])
                    hi += 1
                    
        return sorted(rst)
                
