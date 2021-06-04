# https://leetcode.com/problems/subsets

class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        """Lexicographical (Binary Sorted) Subsets"""
        n = len(nums)
        output = []
        
        for i in range(2**n, 2**(n+1)):
            # generate all len n bitmasks, from 00...000 to 11...111
            bitmask = bin(i)[3:]
            output.append([nums[j] for j in range(n) if bitmask[j] == '1'])
        
        return output
    
    
    def subsets_cascade(self, nums: List[int]) -> List[List[int]]:
        powerset = [[]]
        
        for num in nums:
            powerset += [lst + [num] for lst in powerset]
            
        return powerset
        # Subsets: there are 2**N pcs, because each item either is or is not in the set (no dupls)

        # (there are no duplicate numbers)
        # adding new number to nums
        # --> output len doubles
        # a single num is either in the subset or not
        # we have what we had before + all the subset we had before added with the new num
        
        # example
        # nums = []
        # output = [[]]
        
        # nums = [1]
        # output = [[], [1]]
        
        # nums = [1,2]
        # output = [[], [1], [2], [1, 2]]
        
        # nums = [1,2,3]
        # output = [[], [1], [2], [1, 2], [3], [1,3], [2,3], [1,2,3]]
        #            -- previous ones --, -- prev. lists with the new num appended --