"""

https://leetcode.com/problems/binary-tree-maximum-path-sum
124. Binary Tree Maximum Path Sum
HARD

Recursive DFS
"""

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

"""
Recursive DFS

Key is to understand that a path in the tree can contain at most one split 
(one node where we go to both its left and right children 
-- let's say we traverse from the left to up, then back to right: we never visit same node twice.
If we try to have multiple "splitted nodes", this is no longer possible)

So basically we need to consider each node in the tree as the node where we split.
Then the rest of the nodes must be consider without splitting, i.e. we can only include either their
left or right child (or neither), but not both.
"""

from typing import Optional

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        # instance var to  track the global max path sum seen (the asked result)
        self.max_path_sum = float("-inf")
        
        def dfs(node: Optional[TreeNode]) -> int:
            """
            Keep tracks of the global max path sum (self.max_path_sum), and
            RETURNS the maximum sum without splitting at the node!
            (so retval considers only left, right or neither)
            """
            # base case
            if not node:
                return 0
            
            # recursively find max path sums for left and right (without splitting)
            # note that we don't need to traverse all the way to leaf nodes:
            # in case of negative values, no point including, hence floor to zero
            left_max = max(0, dfs(node.left))
            right_max = max(0, dfs(node.right))
            
            # potentially update max_path_sum with having this node as the split node
            self.max_path_sum = max(self.max_path_sum,
                                    node.val + left_max + right_max)
            
            # return max_path_sum without having this as the split node
            # so considering either left or right, but not both
            return node.val + max(left_max, right_max)
            
            
        dfs(root)  # this set the self.max_sum
        return self.max_path_sum
        