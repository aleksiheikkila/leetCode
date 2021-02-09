class Solution:
    def sortedSquares_trivial(self, nums: List[int]) -> List[int]:
        return sorted([num**2 for num in nums])
    

    def sortedSquares(self, nums: List[int]) -> List[int]:
        # slow...
        rst = []
        pos_ptr = 0
        
        while pos_ptr < len(nums) and nums[pos_ptr] < 0:  # could bisect
            pos_ptr += 1
        pos_starts_idx = pos_ptr
        neg_ptr = pos_starts_idx - 1
            
        # then start there and go towards both start and end
        while len(rst) < len(nums):   
            if neg_ptr < 0:  # out of negatives
                rst.append(nums[pos_ptr] ** 2)
                pos_ptr += 1
                
            elif pos_ptr >= len(nums):  # out of positives
                rst.append(nums[neg_ptr] ** 2)
                neg_ptr -= 1
                
            elif abs(nums[neg_ptr]) < nums[pos_ptr]:
                rst.append(nums[neg_ptr] ** 2)
                neg_ptr -= 1
            else:
                rst.append(nums[pos_ptr] ** 2)
                pos_ptr += 1
                
        
        return rst
        