# https://leetcode.com/explore/learn/card/linked-list/213/conclusion/1225/

"""
# Definition for a Node.
class Node:
    def __init__(self, val, prev, next, child):
        self.val = val
        self.prev = prev
        self.next = next
        self.child = child
"""

class Solution:
    
    def print(self, head):
        if head is None:
            return
        
        node = head
        while node:
            prev_val = node.prev.val if node.prev else None
            next_val = node.next.val if node.next else None
            print(prev_val, node.val, next_val, node.child)
            print("\n")
            
            node = node.next
        
        
    def flatten(self, head: 'Node', verbose=True) -> 'Node':
        
        # process the node
        
        # check if child is not None
        # if child exists, continue from there
        # go depth first
        # backtrack and continue to next
        
        if head is None:
            return None
        
        node = head
        
        while node is not None:
            nextnode = node.next
            
            if node.child is not None:
                head_to_append = self.flatten(node.child, verbose=False)
                #node.child = None
                # set the pointers at the tail
                last_node_to_append = head_to_append
                while last_node_to_append.next is not None:
                    last_node_to_append = last_node_to_append.next
                last_node_to_append.next = nextnode
                nextnode.prev = last_node_to_append
                
                # set the pointers at the head
                head_to_append.prev = node
                node.next = head_to_append
               
                #node.child = None  # did not work for some reason
            node = nextnode
        
        # print the content
        if verbose:
            self.print(head)

        return head
        