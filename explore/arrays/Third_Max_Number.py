
class Solution:
    def thirdMax(self, nums: List[int]) -> int:
        top3 = [float("-inf")] * 3  # max, 2nd, 3rd
        
        for num in nums:
            if num in top3: continue
                
            if num > top3[0]:
                top3 = [num, top3[0], top3[1]]
            elif num > top3[1]:
                top3 = [top3[0], num, top3[1]]
            elif num > top3[2]:
                top3 = [top3[0], top3[1], num]
                
        return max(top3) if float("-inf") in top3 else top3[2]