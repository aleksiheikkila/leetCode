# https://leetcode.com/problems/remove-duplicates-from-sorted-list-ii/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        """Misread the instructions at first: this would keep one occurence of each value
        It asks to get rid of all of the instances of values that occur more than once"""

        if not head:
            return head

        curr = head
        values_seen = set()
        dupls = set()
        
        # Find duplicate values
        while curr:
            if curr.val in values_seen:
                dupls.add(curr.val)
            else:
                values_seen.add(curr.val)
            curr = curr.next
            
            
        # Remove duplicates from the linked list
        curr = head
        tmp_head = ListNode()  # for convenience. The actual head to be returned is tmp_head.next
        prev = tmp_head
        
        while curr:
            if curr.val not in dupls:
                prev.next = curr
                prev = curr
                
            curr = curr.next
        
        prev.next = None
        
        return tmp_head.next
        