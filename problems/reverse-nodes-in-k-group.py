# https://leetcode.com/problems/reverse-nodes-in-k-group/
# Hard

# Linked list

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


from typing import Optional

"""
Illustration

# k=3

dummy->1->2->3->4->5
    p  c

need to reverse 1->2->3

        1->2->3->4->5
  None<-1<-2<-3   
              p c
              
return next_curr: 4, newtail: 1, newhead: 3

"""

class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        
        def has_k_nodes(curr, k) -> bool:
            """Checks if the linked list starting at node curr has at least k nodes in it"""
            if not curr: return False
            
            for _ in range(k-1):
                curr = curr.next
                if not curr: return False
            
            return True
        
        
        def reverse_k_nodes(curr, k):
            """Reverses the group of k nodes starting at node curr.

            Returns next_curr (the node beyound the current group being reversed),
            newhead and newtail, for stitching the reversed llist into its correct place"""
            newtail = curr  # this will be the new tail
            prev = None
            
            for _ in range(k):
                next_ = curr.next  # store this temporarily
                curr.next = prev  # Reversing: current to point to the previous

                # take a step forward
                prev = curr   # current as the new previous
                curr = next_  # current to point to the next one
                
            return curr, prev, newtail
            # so these are next_curr (where to continue processing, 
            # and newhead and newtail of the reversed part
                

        # edge case:
        if not head: return None
        
        dummy = ListNode(val=None, next=head)
        curr = head
        prev = dummy
        
        while has_k_nodes(curr, k):
            next_curr, newhead, newtail = reverse_k_nodes(curr, k)
            
            prev.next = newhead
            newtail.next = next_curr
            
            prev = newtail
            curr = next_curr
        
        # possible remainder: either no nodes or less than k nodes
        # Both are already handled in above while loop
        # where we set newtail.next to the start of the remaining part

        # return the actual head node
        return dummy.next
