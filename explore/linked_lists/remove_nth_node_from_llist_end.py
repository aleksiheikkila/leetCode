# https://leetcode.com/explore/learn/card/linked-list/214/two-pointer-technique/1296/

class Solution:
    # Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        if head is None:
            return head
        
        # Add dummy to handle corner cases
        dummy = ListNode(0)
        dummy.next = head
        
        first = dummy
        second = dummy
        
        # Make gap of n
        for _ in range(n+1):
            first = first.next
            if first is None:
                break
            
        # now just step until the end
        while first is not None:
            first = first.next
            second = second.next
            
        # then delete
        second.next = second.next.next  # if second.next else None
            
        return dummy.next # head, unless it was deleted

        
        
            
 
        
        
            
 