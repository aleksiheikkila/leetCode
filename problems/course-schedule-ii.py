# https://leetcode.com/problems/course-schedule-ii/

# Graph processing.
# Stack

class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        """
        Keep track of available courses (courses with all pre-reqs met)
        
        Take these courses one by one. Keep track of the courses (for the order).
        
        If new courses become available (all pre-reqs met after the most recent course)
        add to available courses.
        In the end, check if we managed to take all courses
        """
        # order in which courses are taken
        taken = []
        
        # Process the graph
        # course is the index. Value is a list of courses following this course
        leads_to = [[] for _ in range(numCourses)]
        num_prereqs = [0 for _ in range(numCourses)]
        for course, prereq in prerequisites:
            leads_to[prereq].append(course)
            num_prereqs[course] += 1
        
        # stack of available courses. Updates as we go
        available = [course for course in range(numCourses)
                         if num_prereqs[course] == 0]
        
        while available:
            course = available.pop()
            taken.append(course)
            
            # check the courses that had this as a pre-req
            for next_course in leads_to[course]:
                num_prereqs[next_course] -= 1
                # if new course unlocked, add to available
                if num_prereqs[next_course] == 0:
                    available.append(next_course)  
            
        return taken if len(taken) == numCourses else []
            