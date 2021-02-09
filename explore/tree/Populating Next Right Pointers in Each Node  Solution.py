# https://leetcode.com/explore/learn/card/data-structure-tree/133/conclusion/994/

"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""



from collections import deque

class Solution:
    def connect(self, root: 'Node') -> 'Node':
        # BFS type
        # Could better utilize the fact that it is a perfect tree
        # This works also for the general case
        if root is None:
            return None
        
        # stack
        s = deque([(root, 1)])  # level
        curr_level = 1
        node = None
        
        while s:
            prev_node, (node, level) = node, s.popleft()
            if level > curr_level:
                # started a new level
                curr_level = level
                prev_node.next = None
            elif prev_node is not None:
                prev_node.next = node
            
            if node.left is not None:
                s.append((node.left, curr_level + 1))
            if node.right is not None:
                s.append((node.right, curr_level + 1))
            
        return root
    