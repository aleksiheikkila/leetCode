# https://leetcode.com/explore/learn/card/binary-search/144/more-practices/1035/

# Doesnt utilize the numbers being sorted

class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        ans = []
        needs = {target - n: i for i, n in enumerate(numbers, start=1)}
        
        for i, num in enumerate(numbers, start=1):
            if num in needs:
                ans.extend([min(i, needs[num]), max(i, needs[num])])
                break

        return ans
    