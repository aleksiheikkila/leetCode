# https://leetcode.com/problems/subsets-ii/

# Now nums with duplicates, but no duplicates allowed to the output

class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        """Lexicographical (Binary Sorted) Subsets"""
        n = len(nums)
        seen = set()
        
        for i in range(2**n, 2**(n+1)):
            # generate all len n bitmasks, from 00...000 to 11...111
            # form the subset by including all ones
            bitmask = bin(i)[3:]
            # add to a set (as immutable tuple, that has been sorted to filter out dupls)
            seen.add(tuple(sorted(nums[j] for j in range(n) if bitmask[j] == '1')))
        
        return [list(t) for t in seen]