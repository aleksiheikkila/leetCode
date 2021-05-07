# https://leetcode.com/problems/diameter-of-binary-tree/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def _depth(self, root: TreeNode):
        depth_left = depth_right = 0
        
        if root.left is not None:
            depth_left = self._depth(root.left)
        if root.right is not None:
            depth_right = self._depth(root.right)
            
        if depth_left + depth_right > self.max_diam:
            self.max_diam = depth_left + depth_right
        
        return max(depth_left+1, depth_right+1)  # for the parent
        
 
    def diameterOfBinaryTree(self, root: TreeNode) -> int:
        # jokaiselle nodelledepth_left ja depth_right
        self.max_diam = 0
        self._depth(root)
        
        return self.max_diam
        