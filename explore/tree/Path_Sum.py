

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    # https://leetcode.com/explore/learn/card/data-structure-tree/17/solve-problems-recursively/537/

    # Given the root of a binary tree and an integer targetSum, 
    # return true if the tree has a root-to-leaf path such that 
    # adding up all the values along the path equals targetSum
        
    def hasPathSum(self, root: TreeNode, targetSum: int) -> bool:
        # Recursively
        if root is None:
            # Should be triggered iff root is None to begin with
            return False
         
        if root.left is None and root.right is None:
            # is leaf 
            if targetSum == root.val: 
                return True
            else:
                return False
          
        return (
            (False if root.left is None else self.hasPathSum(root.left, targetSum - root.val)) or 
            (False if root.right is None else self.hasPathSum(root.right, targetSum - root.val))
                )
        
        
        