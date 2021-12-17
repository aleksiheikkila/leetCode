# https://leetcode.com/problems/merge-k-sorted-lists
# Hard

# Linked lists. Two pointers.
# Kind of merge sort
# Queue

from collections import deque
from typing import List, Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        """Kind of merge sort type of approach, from the bottom up (without the splitting part)"""
        
        def merge_two(llist1, llist2):
            """Given root nodes for two linked lists, merges the linked lists
            together to asc order by reordering the next pointers.
            
            Returns the root node (w smallest value) of the merged linked list.
            """
            # are there edge cases with empty llists etc?
            
            dummy = curr = ListNode(None) # result, the new root, will be dummy.next
            
            # Do until we have no more comparisons
            # Traverse the two linked lists, and add the smaller to curr
            while llist1 and llist2:
                if llist1.val < llist2.val:
                    curr.next = llist1
                    llist1 = llist1.next
                else:
                    curr.next = llist2
                    llist2 = llist2.next
                
                curr = curr.next
            
            # add the rest of the nodes (one of the llists have at least one node)
            curr.next = llist1 if llist1 else llist2

            return dummy.next

        # Edge case
        if not lists: return None
        
        # merge two llists together, until we have only one list left (all merged)
        queue = deque(lists)
        while len(queue) > 1:
            llist1 = queue.popleft()
            llist2 = queue.popleft()
            merged_llist = merge_two(llist1, llist2)
            queue.append(merged_llist)
            
        return queue.pop()
