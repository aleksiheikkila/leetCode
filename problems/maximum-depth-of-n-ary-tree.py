# https://leetcode.com/problems/maximum-depth-of-n-ary-tree

"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    def maxDepth(self, root: 'Node') -> int:
        if root is None:
            return 0
        
        max_d = 0
        s = [(root, 1)]
        
        while s:
            node, level = s.pop()
            if level > max_d:
                max_d = level
            
            if node.children is not None:
                for child in node.children:
                    s.append((child, level + 1))
        
        return max_d
        