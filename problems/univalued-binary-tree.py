# https://leetcode.com/problems/univalued-binary-tree

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isUnivalTree(self, root: Optional[TreeNode]) -> bool:
        val = root.val
        
        s = []  # stack
        if root.left:
            s.append(root.left)
        if root.right:
            s.append(root.right)
        
        while s:
            node = s.pop()
            if node.val != val:
                return False
            if node.left:
                s.append(node.left)
            if node.right:
                s.append(node.right)
        
        return True
