# https://leetcode.com/problems/merge-two-binary-trees

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def mergeTrees(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> Optional[TreeNode]:
        # Recursive

        # Base cases
        # if both root1 and root2 are None, return None
        # else if root1 is None, return root2, and vice versa
        if not root1:
            return root2
        if not root2:
            return root1
        
        # Both nodes exist. Sum their values. Make the root1 the new one
        root1.val += root2.val
        
        # recursively set their left and right
        root1.left = self.mergeTrees(root1.left, root2.left)
        root1.right = self.mergeTrees(root1.right, root2.right)
        
        return root1
        