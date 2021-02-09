# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def searchBST(self, root: TreeNode, val: int) -> TreeNode:
        if root is None:
            return None
        
        if root.val == val:
            return root
        
        left = self.searchBST(root.left, val) 
        if left is not None:
            return left
        right = self.searchBST(root.right, val)
        if right is not None:
            return right
        
        return None
        