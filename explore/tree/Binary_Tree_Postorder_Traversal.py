# https://leetcode.com/explore/learn/card/data-structure-tree/134/traverse-a-tree/930/
# First left subtree, then right, finally root

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    
    def peek(self, stack): 
        if len(stack) > 0: 
            return stack[-1] 
        return None
    
    def postorderTraversal_Iter(self, root: TreeNode) -> List[int]:
        rst = []
        if root is None:
            return rst
        
        nodeStack = []
        while True:
            while root:
                if root.right is not None:
                    nodeStack.append(root.right)
                nodeStack.append(root)
                root = root.left
                
            root = nodeStack.pop()
            if root.right is not None and self.peek(nodeStack) == root.right:
                nodeStack.pop()  # remove root.right from the stack
                nodeStack.append(root)  # add root back to the stack
                root = root.right
                
            else:
                rst.append(root.val)
                root = None
                
            if len(nodeStack) < 1:
                break

        return rst
    
    
    
    def traversalHelper_recu(self, root, rst):
        # recursive
        # visit left subtree, right subtree, node
        if root.left:  self.traversalHelper_recu(root.left, rst)
        if root.right: self.traversalHelper_recu(root.right, rst)
        rst.append(root.val)
    
    def postorderTraversal(self, root: TreeNode) -> List[int]:
        # # recursive
        rst = []
        if root is None:
            return rst
        
        self.traversalHelper_recu(root, rst)
        
        return rst
        