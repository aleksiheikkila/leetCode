# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def preorderTraversal_recursive(self, root: TreeNode) -> List[int]:
        # order: root, left, right
        if root is None:
            return []
        
        rst = []
        
        rst.append(root.val)
        rst.extend(self.preorderTraversal(root.left))
        rst.extend(self.preorderTraversal(root.right))
        
        return rst
    
    
    def preorderTraversal_iter(self, root: TreeNode) -> List[int]:
        # order: root, left, right
        if root is None:
            return []
        
        rst = []
        nodeStack = [root]
        
        while nodeStack:
            node = nodeStack.pop()
            rst.append(node.val)
            if node.right: nodeStack.append(node.right)
            if node.left:  nodeStack.append(node.left)
        
        return rst
        