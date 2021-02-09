# https://leetcode.com/explore/learn/card/fun-with-arrays/511/in-place-operations/3259/

class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        if arr is None or len(arr) == 0:
            return arr
        
        max_seen = arr[len(arr)-1] 
        arr[len(arr)-1] = -1
        
        for i in range(len(arr)-2, -1, -1):
            arr[i], max_seen = max_seen, max(max_seen, arr[i])
 
        return arr