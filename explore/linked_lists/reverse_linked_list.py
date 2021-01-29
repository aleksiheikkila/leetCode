# https://leetcode.com/explore/learn/card/linked-list/219/classic-problems/1205/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        # iterative
        # reverse the next link directions, return the last node
        prev = None
        curr = head
        
        while curr is not None:
            nxt = curr.next
            curr.next = prev
            
            prev = curr
            curr = nxt
            
        return prev  
    # curr is the next of the last node, i.e. None. So return prev = lastNode = head of the reversed
            
            
            
            
        