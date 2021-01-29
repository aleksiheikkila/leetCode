# https://leetcode.com/explore/learn/card/linked-list/219/classic-problems/1208/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def oddEvenList(self, head: ListNode) -> ListNode:
        # form separate even odd llists, then put them together
        if head is None:
            return head
        
        # Dummy heads
        odds_head = ListNode()
        evens_head = ListNode()
        # Pointers
        curr_node_odds = odds_head
        curr_node_evens = evens_head  
        node = head
        
        isOdd = True
        while node:
            if isOdd:
                curr_node_odds.next = node
                curr_node_odds = node
            else:
                curr_node_evens.next = node
                curr_node_evens = node

            isOdd = not isOdd
            node = node.next
            
        curr_node_evens.next = None  # last even should point to nothing (end of linked list)
        curr_node_odds.next = evens_head.next  # tie together, get rid of the dummy
        
        return odds_head.next  # odds_head is the dummy
            