# https://leetcode.com/problems/house-robber-iii/

# each house has one and only one parent house (except for root)
# cannot select two directly linked nodes

# # Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution:
    memo = {}  # memoization
    
    def rob(self, root: TreeNode) -> int:
        """Recursive"""
        # base case
        if root is None:
            return 0
        
        if root in self.memo:
            # if we have already calculated the value
            return self.memo[root]
        
        s = root.val
        
        # skip the next level
        if root.left is not None:
            s += self.rob(root.left.left) 
            s += self.rob(root.left.right)
        if root.right is not None:
            s += self.rob(root.right.left) 
            s += self.rob(root.right.right)
        
        # Calculate the same, starting from the next level
        next_s = self.rob(root.left) + self.rob(root.right)
        
        # combine and memoize
        rst = max(s, next_s)
        self.memo[root] = rst
        
        return rst
        
