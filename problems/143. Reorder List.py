""" 143. Reorder List
MEDIUM 
https://leetcode.com/problems/reorder-list/

You are given the head of a singly linked-list. The list can be represented as:

L0 → L1 → … → Ln - 1 → Ln
Reorder the list to be on the following form:

L0 → Ln → L1 → Ln - 1 → L2 → Ln - 2 → …
You may not modify the values in the list's nodes. Only nodes themselves may be changed.
"""

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        1 -> 4 -> 2 -> 3 - 5
        
        Find the middle of the list using slow and fast pointers.
        Reverse the links in the 2nd half
        """
        
        # Finding the middle of the linked list
        slow, fast = head, head.next
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            
        # beginning of the 2nd half is slow.next
        # (slow stops at the last element of the 1st half in case of even num of nodes
        # or at the middle element in case of odd num of nodes)
        
        # Reversing the links in the second half of the original linked list
        second_half_node = slow.next
        slow.next = None  # this will end up being the last element
        prev = None
        
        while second_half_node:
            next_node = second_half_node.next
            second_half_node.next = prev
            prev, second_half_node = second_half_node, next_node
            
        
        # Then merge
        first, second = head, prev  # prev is the original last node in the 2nd half
        while second:  # second is possibly smaller
            tmp1, tmp2 = first.next, second.next
            first.next = second
            second.next = tmp1
            first, second = tmp1, tmp2
        

    
    def reorderList2(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        1 -> 4 -> 2 -> 3
        """
        
        # Straightforward way. Collect nodes and then smash them together in the correct order
        # Slow
        nodes = []
        node = head
        while node:
            nodes.append(node)
            node = node.next
            
        l, r = 1, len(nodes) - 1
        curr = head
        from_back = True
        
        while l <= r:
            curr.next = nodes[r] if from_back else nodes[l]
            curr.next.next = None
            curr = curr.next
            if from_back:
                r -= 1
            else:
                l += 1
            from_back = not from_back
            
        