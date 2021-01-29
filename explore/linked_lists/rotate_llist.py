# https://leetcode.com/explore/learn/card/linked-list/213/conclusion/1295/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:       
    def rotateRight(self, head: ListNode, k: int) -> ListNode:
        if head is None:
            return None
        
        # Get llist length and prior tail node
        l = 1
        old_tail = head
        while old_tail.next:
            l += 1
            old_tail = old_tail.next
              
        move_right_by = k % l
        
        if move_right_by == 0:
            return head
        
        # then find the new head
        new_head_idx = l - move_right_by
        
        # find the new tail and head nodes
        new_tail = head
        for _ in range(new_head_idx - 1):
            new_tail = new_tail.next
        new_head = new_tail.next
        
        # adjust pointers
        new_tail.next = None
        old_tail.next = head 
        
        return new_head
        
        