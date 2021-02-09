# https://leetcode.com/explore/learn/card/data-structure-tree/133/conclusion/932/

# Given a binary tree, find the lowest common ancestor (LCA) of two given nodes in the tree.
# The lowest common ancestor is defined between two nodes p and q as the lowest node in T 
# that has both p and q as descendants (where we allow a node to be a descendant of itself).

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution:
    
    def find_path_to(self, root: 'TreeNode', targetNode: 'TreeNode'):
        # # SUPER SLOW DUE TO MAKING ALL THOSE LISTS - as expected
        # DFS
        if root is None:
            return None
        s = [[root]]
        
        while s:
            path = s.pop()
            node = path[-1]

            if node == targetNode:
                return path
            if node.left is not None:
                new_item = path.copy()
                new_item.append(node.left)
                s.append(new_item)
            if node.right is not None:
                new_item = path.copy()
                new_item.append(node.right)
                s.append(new_item)
        
        return None
        
    
    def find_path_to_rec(self, root, node):
        # more efficient but not that great
        # Would be better to search for both nodes at the same time (no need to traverse same branches twice)
        if root is None:
            return None

        if root == node:
            return [node]
        
        rst_left = self.find_path_to_rec(root.left, node)
        rst_right = self.find_path_to_rec(root.right, node)
        
        if rst_left is not None:
            rst_left.append(root)
            return rst_left
        if rst_right is not None:
            rst_right.append(root)
            return rst_right
        
        return None
    
        
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':     
        path_to_p_rec = self.find_path_to_rec(root, p)
        path_to_q_rec = self.find_path_to_rec(root, q)

        for n1, n2 in zip(path_to_p_rec[::-1], path_to_q_rec[::-1]):
            if n1 == n2:
                last_common = n1
            else:
                break
        
        return last_common