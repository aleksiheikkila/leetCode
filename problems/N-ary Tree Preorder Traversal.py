# https://leetcode.com/explore/featured/card/april-leetcoding-challenge-2021/595/week-3-april-15th-april-21st/3714/

"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children  # this is a list of nodes!
"""

class Solution:
    def preorder(self, root: 'Node') -> List[int]:
        # The N-ary tree is a tree that allows us to have n number of children for a node
        vals = []
        stack = None if root is None else [root]
        
        while stack:
            node = stack.pop()
            vals.append(node.val)
            stack.extend(node.children[::-1])
        
        return vals
