# https://leetcode.com/explore/learn/card/linked-list/213/conclusion/1227/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        n1 = l1
        n2 = l2
        
        new_llist_head = ListNode()  # dummy node at the beginning
        node = new_llist_head
        
        while any((n1, n2)):
            # end when both None
            if n1 is None:
                node.next = n2
                n2 = n2.next
            elif n2 is None:
                node.next = n1
                n1 = n1.next
            else:
                # both nodes exist, select next node by val
                if  n1.val < n2.val:
                    node.next = n1
                    n1 = n1.next  
                else:
                    node.next = n2
                    n2 = n2.next 
                    
            node = node.next

        return new_llist_head.next
        