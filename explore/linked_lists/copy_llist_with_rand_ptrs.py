# https://leetcode.com/explore/learn/card/linked-list/213/conclusion/1229/

"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Node') -> 'Node':
        if head is None:
            return None
        
        new_head = Node(head.val)
        new_curr = new_head
        
        newnodes = {0: new_head}  # index to node map
        oldnode_to_idx = {head: 0}  # node to idx map
        node = head.next
        
        idx = 1
        while node is not None:
            oldnode_to_idx[node] =  idx
            
            newnode = Node(node.val)
            newnodes[idx] = newnode

            new_curr.next = newnode
            new_curr = newnode
            
            node = node.next
            idx += 1
        
        # then iterate and add the random pointers
        newnode = new_head
        oldnode = head
        
        while newnode and oldnode:
            if oldnode.random:
                newnode.random = newnodes[oldnode_to_idx[oldnode.random]]
            
            newnode = newnode.next
            oldnode = oldnode.next
        
        return new_head
        