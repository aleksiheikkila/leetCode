# https://leetcode.com/problems/reverse-linked-list-ii

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        
        dummy_head = ListNode(next=head)  # does this help here?
        
        # go to the starting pos
        node_num = 1
        curr = dummy_head.next  # i.e. head
        prev = dummy_head
        while curr and node_num < left:
            node_num += 1
            curr, prev = curr.next, curr
        
        # if there is not those nodes that needs to be reversed
        if not curr:
            return head
        
        last_node_in_unchanged_left = prev
        first_reversed_node = curr  # this is the first node of those that we need to reverse
        
        #print("last node val in unc left", last_node_in_unchanged_left.val)
        #print("first node in reversed part", start_node.val)
        
        while curr and node_num < right + 1:
            #print(node_num, curr.val)
            
            if node_num == left:
                # do not change next for the first one
                curr, prev = curr.next, curr
            
            else:
                # reverse
                nxt = curr.next
                curr.next = prev
                # move to next one in the original sequence
                curr, prev = nxt, curr
                
            node_num += 1

        first_node_in_unchanged_right = curr
        last_reversed_node = prev  # last node in
        
        last_node_in_unchanged_left.next = last_reversed_node
        first_reversed_node.next = first_node_in_unchanged_right
        
        return dummy_head.next
        