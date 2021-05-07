# https://leetcode.com/explore/challenge/card/may-leetcoding-challenge-2021/598/week-1-may-1st-may-7th/3729/

from queue import PriorityQueue

# Slow but accepted 

class Solution:
    def scheduleCourse(self, courses: List[List[int]]) -> int:
        
        courses = sorted(courses, key=lambda x: x[1])
        # Starting point. Take earliest end times first.
        
        prioQ = PriorityQueue()  # courses taken
        time = 0
        
        for course in courses:
            if (time + course[0]) <= course[1]:
                # ok to take this course
                prioQ.put(-course[0]) # gets the smallest
                time += course[0]
                
            elif not prioQ.empty():
                # swap with the longest course taken so far (with stricter end date), 
                # if is longer than current
                max_dur = -prioQ.get()
                if max_dur > course[0]:
                    prioQ.put(-course[0])
                    time += course[0] - max_dur  # adjust the time
                else:
                    prioQ.put(-max_dur)
                    
        return prioQ.qsize()  # "approximate size", refers only to possible concurrent changes that are not a problem here
        