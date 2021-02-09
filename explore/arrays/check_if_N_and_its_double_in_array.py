# https://leetcode.com/explore/learn/card/fun-with-arrays/527/searching-for-items-in-an-array/3250/

class Solution:
    def checkIfExist(self, arr: List[int]) -> bool:
        if arr is None or len(arr) < 2:
            return False
        
        seen = set()
        for num in arr:
            if num*2 in seen or num/2 in seen:
                return True
            seen.add(num)
            
        return False
        