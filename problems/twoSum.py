class Solution:
    def twoSum_naive(self, nums: List[int], target: int) -> List[int]:
        # Brute Force. O(n^2)
        for i, a in enumerate(nums[:-1]):
            for j, b in enumerate(nums[i+1:], start=i+1):
                if a+b == target:
                    return [i, j]
    
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # Hashmap-based
        # O(n)

        # hashmap with complement as a key, index as a value
        complements = {target - num: idx for idx, num in enumerate(nums)}

        for idx, num in enumerate(nums):
            compl = complements.get(num)
            if compl and compl != idx:
                return [idx, compl]