# https://leetcode.com/problems/insert-interval
# Medium

from collections import List


class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        
        rst = []
        
        for i in range(len(intervals)):
            # if newInterval ends before current starts, insert new before current
            # then add all the rest and return
            if newInterval[1] < intervals[i][0]:
                rst.append(newInterval)
                return rst + intervals[i:]
            
            # if new starts after the current interval: add current but not yet the new
            elif newInterval[0] > intervals[i][1]:
                rst.append(intervals[i])
                
            # else: new overlaps with the current
            else:
                # merge newInterval with the current, to make a new newInterval :)
                # we keep on going here until we have merged all overlapping ones
                # after that we should either run out of intervals 
                # (merged will be the last one and needs to be still added to rst)
                # OR, we run into the first condition, append newInterval + all following ones and return
                newInterval = [min(newInterval[0], intervals[i][0]),
                               max(newInterval[1], intervals[i][1])]
        
        rst.append(newInterval)
        
        return rst
    