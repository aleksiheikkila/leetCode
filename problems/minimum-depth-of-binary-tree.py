# https://leetcode.com/problems/minimum-depth-of-binary-tree

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from collections import deque

class Solution:
    # depth first
    def _depth(self, node):
        if node is None:
            return 0
        
        if node.left is None and node.right is None:
            # leaf node
            return 1

        return 1 + min(self._depth(node.left) if node.left else float("inf"), 
                       self._depth(node.right) if node.right else float("inf"))
    
    
    def minDepth_dfs(self, root: TreeNode) -> int:
        
        return self._depth(root)

    # BFS is better
    def minDepth(self, root: TreeNode) -> int:
        if root is None:
            return 0

        q = deque([(root, 1)])  # node, level

        while q:
            node, depth = q.popleft()
            if node:
                if node.left is None and node.right is None:
                    # first leaf... eventually this is reached
                    return depth
                q.append((node.left, depth + 1))
                q.append((node.right, depth + 1))
            




        