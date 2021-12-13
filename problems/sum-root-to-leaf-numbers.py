# https://leetcode.com/problems/sum-root-to-leaf-numbers

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        rst = 0
        
        # dfs traversal, keep track of the sum so far from the root
        # when at leaf, add to rst
        
        stack = [(root, 0)]  # (node, sum_so_far)
        while stack:
            node, sum_so_far = stack.pop()
            sum_so_far = 10*sum_so_far + node.val
            
            if not node.left and not node.right:
                rst += sum_so_far
            else:
                if node.left:  stack.append((node.left, sum_so_far))
                if node.right: stack.append((node.right, sum_so_far))
        
        return rst
        