# https://leetcode.com/problems/maximum-product-of-splitted-binary-tree/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxProduct(self, root: Optional[TreeNode]) -> int:
        
        # calculate sum of values for each node (incl. vals under it)
        # calculate the total sum
        
        # then for each node, check what is the sum * (total - sum)
        
        if not root:
            return 0
        
        #self.vals = set()
        self.vals = []
        self.sum_at(root)
        
        total = self.vals[-1]
        #total = max(self.vals)
        
        return max(val * (total - val) for val in self.vals) % (10**9 + 7)
        
        
    # dfs    
    def sum_at(self, root) -> int:
        """returns sum at node root, which includes that nodes value + sum of vals under it
        also stores those to vals list"""
        if root is None:
            return 0
        else:
            val_at_node = root.val + self.sum_at(root.left) + self.sum_at(root.right)
            self.vals.append(val_at_node)
            return val_at_node
            