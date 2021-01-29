
class Solution:
    # Contains Duplicate 1:
    def containsDuplicate(self, nums: List[int]) -> bool:
        return len(set(nums)) != len(nums)
        

    # Contains DUplicate 2
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        
        num_to_idx = {}  # num as key, index of its latest occurence as val
        # "Have we seen the number, where?"
        
        for i in range(len(nums)):
            if nums[i] in num_to_idx and i - num_to_idx[nums[i]] <= k:
                return True
            else:
                num_to_idx[nums[i]] = i

        return False
        
        
        
    