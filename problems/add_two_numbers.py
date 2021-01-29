# https://leetcode.com/problems/add-two-numbers

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        node1 = l1
        node2 = l2
        carry = 0
        prev_node = None
        
        while node1 or node2 or carry:
            d1 = node1.val if node1 else 0
            d2 = node2.val if node2 else 0 
            carry, remainder = divmod(d1+d2+carry, 10)
            
            new_node = ListNode(remainder)
            
            if not prev_node:
                root = ListNode(remainder)
                prev_node = root
            else:
                new_node = ListNode(remainder)
                prev_node.next = new_node
                prev_node = new_node
                
            
            node1 = node1.next if node1 else None
            node2 = node2.next if node2 else None
            
        return root
        