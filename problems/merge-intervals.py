# https://leetcode.com/problems/merge-intervals

class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        
        actions = []
        
        for iv in intervals:
            actions.append((iv[0], 1))
            actions.append((iv[1], -1))
            
        actions.sort(key = lambda x: (x[0], -x[1]))  # +1 "booking" first before -1 "return"
        
        iv_start = None
        intervals_on = 0
        merged_intervals = []
        
        for act in actions:
            if act[1] == 1:
                # interval starts
                if intervals_on == 0:
                    # new block starting
                    iv_start = act[0]

                intervals_on += 1
            
            if act[1] == -1:
                # original interval ending
                if intervals_on < 1:
                    raise ValueError("ohnoh")
                elif intervals_on == 1:
                    merged_intervals.append([iv_start, act[0]])
                
                intervals_on -= 1
                
        return merged_intervals
                        