# https://leetcode.com/problems/queue-reconstruction-by-height
# Medium

# Sort and place them into the right position in the array (queue)

"""
Example
[7,0],[4,4],[7,1],[5,0],[6,1],[5,2]]


First, sort by height to desc and k asc:
=> [7,0], [7,1], [6,1], [5,0], [5,2], [4,4]]

queue = []
Take persons one by one.

Just insert the person into kth position!
(as we have placed already everyone taller, 
and persons with same height but less people in front of them)

Like so:
Process [7, 0]
queue.insert(0, [7, 0]) => [[7, 0]]

Process [7, 1]
queue.insert(1, [7, 1]) => [[7, 0], [7, 1]]

Process [6, 1]
queue.insert(1, [6, 1]) => [[7, 0], [6, 1], [7, 1]]

Process [5, 0]
queue.insert(0, [5, 0]) => [[7, 0], [6, 1], [7, 1]]

etc.
"""

from typing import List

class Solution:
    def reconstructQueue(self, people: List[List[int]]) -> List[List[int]]:
        queue = []
        
        for person in sorted(people, key=lambda x: (-x[0], x[1])):
            queue.insert(person[1], person)
            
        return queue
        