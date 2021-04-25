# https://leetcode.com/explore/learn/card/binary-search/137/conclusion/977/
#  find the smallest element in the list that is larger than the given target

class Solution:
    def nextGreatestLetter(self, letters: List[str], target: str) -> str:
        let = letters + [letters[0]]
        left, right = 0, len(let)-1
        
        while left < right:
            mid = (left + right) // 2
            c = let[mid]

            if c <= target:
                left = mid + 1
            else:
                right = mid

        return let[right]
        