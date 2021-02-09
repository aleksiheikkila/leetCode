# https://leetcode.com/explore/learn/card/data-structure-tree/134/traverse-a-tree/931/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from collections import deque

class Solution:
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        rst = []
        if root is None:
            return rst
        
        curr_level = 1  # level in the tree. 1 is the root level
        q = deque([(root, 1)])
        rst_level = []  # values for a level
        
        while q:
            node, level = q.popleft()
            if level > curr_level:  # entered a new level
                rst.append(rst_level)
                rst_level = []
                curr_level = level            
            rst_level.append(node.val)
            if node.left is not None: 
                q.append((node.left, level + 1))
            if node.right is not None:
                q.append((node.right, level + 1))
                
        # finally, add the rst of the last level if it is not empty
        if len(rst_level) > 0:
            rst.append(rst_level)
                
        return rst
        