# https://leetcode.com/problems/partition-equal-subset-sum

class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        # So basically if the sum of nums is x, we need to partition nums into subsets 
        # that sum to x/2, x/2, i.e. half of the sum (sum clearly needs to be even)
        
        # when we find one partition, the rest of the elements make up the other part.
        # so basically: can we find a sum of any elements that is equal to sum/2
        
        target = sum(nums)
        # Optimization: if sum is odd, partitioning is not doable
        if target % 2 == 1:
            return False
        target /= 2  # actual target
        
        dp = set([0])  # this contains all possible sums formed so far
        
        for num in nums:
            new_dp = set(dp)  # use another temp set because of the below set iteration
            for val in dp:
                # stop as soon as possible
                if val + num == target:
                    return True
                new_dp.add(val + num)
                
            dp = new_dp
        
        # If we ended up here, there was no way to do the partitioning
        return False
        