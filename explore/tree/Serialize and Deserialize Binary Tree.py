# https://leetcode.com/explore/learn/card/data-structure-tree/133/conclusion/995/

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

from collections import deque

class Codec:
    def serialize(self, root):
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """
        if root is None:
            return ""
        
        ser = []
        q = deque([root])
        last_valid_idx = -1  # getting rid of the trailing Nones
        
        while q:
            node = q.popleft()
            if node is None:
                ser.append(None)
            else:
                ser.append(node.val)
                valid_slice_end = len(ser)
                q.append(node.left)
                q.append(node.right)

        return str(ser[:valid_slice_end])
        

    def deserialize(self, data, verbose=False):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """        
        # assumes correct format
        if len(data) < 3:
            return None
        
        vals = data[1:-1].split(", ")  # cast to int later
        
        if vals[0] == "None":
            return None
        
        root = TreeNode(int(vals[0]))  # return this
        q = deque()
        node = root
        i = 1
        
        while i <= len(vals) - 1:
            left = vals[i]
            right = vals[i+1] if i+1 < len(vals) else "None"
            i += 2
            
            if left != "None":
                node.left = TreeNode(int(left))
                q.append(node.left)
            if right != "None":
                node.right = TreeNode(int(right))
                q.append(node.right)
            node = q.popleft()
        
        if verbose:
            nodes = deque([root])
            print("Printing nodes...")
            while nodes:
                node = nodes.popleft()

                lft = node.left.val if node.left else None
                rgt = node.right.val if node.right else None
                print("val: ",node.val, "  -  left:", lft, "  -  right:", rgt)
                if node.left:
                    nodes.append(node.left)
                if node.right:
                    nodes.append(node.right)

        return root
        

# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# ans = deser.deserialize(ser.serialize(root))