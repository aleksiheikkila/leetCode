# https://leetcode.com/problems/remove-duplicates-from-sorted-list

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        if not head:
            return head
        
        prev, curr = head, head.next
        
        while curr is not None:
            if curr.val != prev.val:
                prev.next = curr
                prev = curr
            curr = curr.next
        
        prev.next = None
        return head
