class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        # with a sorted array and three pointers
        # O(n^2)
        triplets = []
        target = 0
        
        nums.sort()
        
        for i in range(len(nums) - 2):  # 'current' pointer:
            
            # if same number, skip to avoid duplicates
            if i > 0 and nums[i] == nums[i - 1]: continue
            
            left = i + 1
            right = len(nums) - 1
            
            
            while left < right:
                curr_sum = nums[i] + nums[left] + nums[right]
                if curr_sum == target:
                    triplets.append([nums[i], nums[left], nums[right]])
                    
                    # Avoid duplicates:
                    while left < right and nums[left] == nums[left + 1]:
                        left += 1
                    while left < right and nums[right] == nums[right - 1]:
                        right -= 1
                    
                    left += 1
                    right -= 1
                elif curr_sum < target:
                    # increase left
                    left += 1
                else:
                    # current sum larger than target, decrease right
                    right -= 1
        
        # Remove duplicates (avoiding them is more efficient)
        #return [list(x) for x in set(tuple(triplet) for triplet in triplets)]
        return triplets