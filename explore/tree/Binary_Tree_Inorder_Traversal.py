# https://leetcode.com/explore/learn/card/data-structure-tree/134/traverse-a-tree/929/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal_rec(self, root: TreeNode) -> List[int]:
         # recursive
        rst = []
        if root is None:
            return rst
        
        rst.extend(self.inorderTraversal(root.left))
        rst.append(root.val)
        rst.extend(self.inorderTraversal(root.right))
        # tai helper func joka ottaa listan, jota muokataan suoraan
        
        return rst
    
    
    def inorderTraversal_iter(self, root: TreeNode) -> List[int]:
        # iterative
        rst = []
        if root is None:
            return rst
        
        curr = root
        nodeStack = []
        
        # GO as far left as possible, adding nodes to stack
        # Then report one val from stack, then go to its right
        # Fallback option to pop from stack
        while curr is not None or len(nodeStack) > 0:
            while curr is not None:
                nodeStack.append(curr)
                curr = curr.left
                
            # ok nyt curr on None: Otetaan stackista edellinen
            curr = nodeStack.pop()
            rst.append(curr.val)
            curr = curr.right
            
        return rst
            