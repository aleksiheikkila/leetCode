# https://leetcode.com/problems/remove-covered-intervals
# Medium

# Sort + line sweep

"""
First, sort intervals to
    1. starting_time ascending
    2. ending_time descending 
        (to handle intervals having same starting time: biggest end time can cover the others)
(nlog(n))

Then, line sweep over intervals.

the invervals processed prior have starting_time not later than the current interval.
That we dont need to check.
We need to check if the current interval's ending time is larger that the max seen so far.
In that case it is not covered.
"""

class Solution:
    def removeCoveredIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort(key=lambda x: (x[0], -x[1]))
        
        num_noncovered = 0
        max_end_time_so_far = 0
        
        for _, end in intervals:
            if end > max_end_time_so_far:
                num_noncovered += 1
                max_end_time_so_far = end

        return num_noncovered
        