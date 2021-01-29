# https://leetcode.com/explore/learn/card/linked-list/219/classic-problems/1207/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeElements(self, head: ListNode, val: int) -> ListNode:
        prev = None
        curr = head
        
        while curr is not None:
            if curr.val == val:
                # remove
                if prev is None:
                    head = curr.next
                    curr = head
                    continue
                else:
                    prev.next = curr.next
                    curr = curr.next
                    continue
            
            
            prev, curr = curr, curr.next
               
        return head
        