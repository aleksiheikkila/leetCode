# https://leetcode.com/problems/course-schedule
# Graph processing, DFS, cycle detection

from collections import defaultdict
from typing import List

class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        # graph processing. Adjacencies
        prereqs = defaultdict(list)
        for course, prereq in prerequisites:
            prereqs[course].append(prereq)
            
        can_be_taken = set()  # courses that can be taken. To avoid duplicate processing
        path = set()  # courses in the current traversal path.
            
        def dfs(course: int) -> bool:
            """Returns true if course can be taken, false if not (i.e. contains a loop)"""
            # Base cases
            # 1. Already processed and can be taken. Short-circuit
            if course in can_be_taken: return True
            # 2. Already in path: cycle detected!
            if course in path: return False
            
            path.add(course)
            for prereq_course in prereqs[course]:
                if not dfs(prereq_course): return False
            # If we have not yet returned False, it means this course can be taken. All pre-reqs OK
            can_be_taken.add(course)
            
            # backtrack, so remove course from current path
            path.remove(course)
            return True
        
        # need to loop all courses, in case the graph has isolated components
        for course in range(numCourses):
            if not dfs(course): return False
            
        return True
        