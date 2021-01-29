# https://leetcode.com/explore/learn/card/linked-list/219/classic-problems/1209/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def isPalindrome(self, head: ListNode) -> bool:
        # Stack based approach. Two passes, mem: 0(N)
        stack = []
        node = head
        sz = 0
        while node:
            stack.append(node.val)
            node = node.next
            sz += 1
            
        # start matching
        node = head
        i = 0
        while node and i < sz/2:
            if node.val != stack.pop():
                return False
            node = node.next
            
        return True