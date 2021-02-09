# https://leetcode.com/explore/learn/card/data-structure-tree/133/conclusion/942/
# Slow-ish

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# a) Inorder (Left, Root, Right)
# (b) Preorder (Root, Left, Right)
# (c) Postorder (Left, Right, Root)
# Breadth First or Level Order Traversal... all nodes on the same level before going deeper


class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> TreeNode:
        # a) Inorder (Left, Root, Right)
        # c) Postorder (Left, Right, Root)
        
        # Main idea: 
        # last element of postorder is the root
        # Find the same value from inorder list. Left side of this will be left child, right side right.
        # The same above number of elements will be put into postorder lists (left side to left, right to right)
        # repeat
        
        if len(inorder) == 0 or len(postorder) == 0:
            return None
        
        root = TreeNode(val=postorder.pop()) # last one in the postorder is the root
        inorder_root_idx = inorder.index(root.val)
        
        # Would be faster to use indices and not create new lists repeatedly
        inorder_right = inorder[inorder_root_idx+1:]        
        inorder_left = inorder[:inorder_root_idx]
        
        postorder_right = postorder[len(inorder_left):len(postorder)]
        postorder_left = postorder[:len(inorder_left)]
        
        root.right = None if len(inorder_right) == 0 else self.buildTree(inorder_right, postorder_right)
        root.left = None if len(inorder_left) == 0 else self.buildTree(inorder_left, postorder_left)
        
        return root
        