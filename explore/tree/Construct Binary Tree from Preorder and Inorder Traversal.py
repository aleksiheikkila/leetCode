# https://leetcode.com/explore/learn/card/data-structure-tree/133/conclusion/943/
# Slow due to repeated list creation (replace by just using indices)

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> TreeNode:
        if len(preorder) == 0 or len(inorder) == 0:
            return None
        
        # root is the first elem in preorder
        root = TreeNode(val = preorder[0])
        inorder_root_idx = inorder.index(root.val)
        
        inorder_left = inorder[:inorder_root_idx]
        inorder_right = inorder[inorder_root_idx+1:]
        
        preorder_left = preorder[1:len(inorder_left)+1]
        preorder_right = preorder[len(inorder_left)+1:]
        
        root.left = None if len(inorder_left) == 0 else self.buildTree(preorder_left, inorder_left)
        root.right = None if len(inorder_right) == 0 else self.buildTree(preorder_right, inorder_right)
        
        return root
        