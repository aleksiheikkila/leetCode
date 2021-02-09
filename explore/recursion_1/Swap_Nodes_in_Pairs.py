# https://leetcode.com/explore/learn/card/recursion-i/250/principle-of-recursion/1681/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

# First, we swap the first two nodes in the list, i.e. head and head.next;
# Then, we call the function self as swap(head.next.next) to swap the rest of the list following the first two # nodes.
# Finally, we attach the returned head of the sub-list in step (2) with the two nodes swapped in step (1) to form a new linked list.

class Solution:
    def swapPairs(self, head: ListNode) -> ListNode:
        if head is None or head.next is None:
            return head

        old_head, head = head, head.next
        old_head.next, head.next = old_head.next.next, old_head
        old_head.next = self.swapPairs(old_head.next)

        return head
    