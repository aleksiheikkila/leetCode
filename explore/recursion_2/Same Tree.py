# https://leetcode.com/explore/learn/card/recursion-ii/503/recursion-to-iteration/2894/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSameTree(self, p: TreeNode, q: TreeNode) -> bool:
        # Given the roots of two binary trees p and q, write a function to check if they are the same or not.
        
        if p is None and q is None:
            return True
        if p is None or q is None:
            return False
        if p.val != q.val:
            return False
        
        return self.isSameTree(p.left, q.left) and \
               self.isSameTree(p.right, q.right)
        