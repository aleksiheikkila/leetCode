# https://leetcode.com/explore/learn/card/recursion-ii/470/divide-and-conquer/2874/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from math import inf

class Solution:
    def isValidBST(self, root: TreeNode) -> bool:
        def validate(node, lo=-inf, hi=inf) -> bool:
            if node is None:
                return True
        
            # curr node's val must be between lo and hi (keep track of these)
            if node.val >= hi or node.val <= lo:
                return False

            return (validate(node.left, lo=lo, hi=node.val) and 
                    validate(node.right, lo=node.val, hi=hi))
    
    
        return validate(root)
