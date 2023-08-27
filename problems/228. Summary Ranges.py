""" 228. Summary Ranges
Easy


You are given a sorted unique integer array nums.

A range [a,b] is the set of all integers from a to b (inclusive).

Return the smallest sorted list of ranges that cover all the numbers in the array exactly. 
That is, each element of nums is covered by exactly one of the ranges, and there is no integer 
x such that x is in one of the ranges but not in nums.

Each range [a,b] in the list should be output as:

"a->b" if a != b
"a" if a == b

"""

class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        if len(nums) == 0:
            return []
        
        if len(nums) == 1:
            return [str(nums[0])]
        
        ranges = []
        start = prev = nums[0] 
        
        for num in nums[1:]:
            if num != prev + 1:
                # a gap
                if prev == start:
                    ranges.append(str(start))
                else:
                    ranges.append(f"{start}->{prev}")
                start = num     
            prev = num
        
        # add the last one
        if prev == start:
            ranges.append(str(start))
        else:
            ranges.append(f"{start}->{prev}")
        
        return ranges
        