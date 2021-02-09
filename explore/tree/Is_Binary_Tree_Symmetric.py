# https://leetcode.com/explore/learn/card/data-structure-tree/17/solve-problems-recursively/536/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from collections import deque

class Solution:
    def isSymmetric(self, root: TreeNode) -> bool:
        # a stack with left and right pair
        if root is None:
            return True
        
        childpair_nones = sum(node is None for node in (root.left, root.right))
        if childpair_nones == 1:
            return False
        elif childpair_nones == 0:
            d = deque([(root.left, root.right)])
            while d:
                left, right = d.popleft()
                if left.val != right.val:
                    return False

                childpair_nones = sum(node is None for node in (left.left, right.right))
                if childpair_nones == 1:
                    return False
                elif childpair_nones == 0:
                    d.append((left.left, right.right))

                childpair_nones = sum(node is None for node in (left.right, right.left))
                if childpair_nones == 1:
                    return False
                elif childpair_nones == 0:
                    d.append((left.right, right.left))
            
        return True
        