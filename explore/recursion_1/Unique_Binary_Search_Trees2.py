# https://leetcode.com/explore/learn/card/recursion-i/253/conclusion/2384/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def generateTrees(self, n: int) -> List[TreeNode]:
        # left.val < val < right.val
        if n == 0:
            return []
        
        return self.getTrees(1, n)

    
    def getTrees(self, left: int, right: int):
        trees = []
        
        if left > right:
            return [None]  # need to give this 
        # pick a node, split to left and right portion and recurse
        for nodeVal in range(left, right + 1):
            leftTrees = self.getTrees(left, nodeVal - 1)  # [list of nodes]
            rightTrees = self.getTrees(nodeVal + 1, right)
            for leftNode in leftTrees:
                for rightNode in rightTrees:
                    node = TreeNode(nodeVal)
                    node.left = leftNode
                    node.right = rightNode
                    trees.append(node)
        
        return trees
