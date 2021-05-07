# https://leetcode.com/explore/challenge/card/may-leetcoding-challenge-2021/598/week-1-may-1st-may-7th/3733/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    
    def get_mid(self, head) -> ListNode:
        """Helper. Get middle ListNode from the linked list. Cuts the link leading to it"""
        if head.next is None:
            return head

        slow = fast = prev = head

        while fast and fast.next:
            slow, prev = slow.next, slow
            fast = fast.next.next

        prev.next = None
        
        return slow  # this is the mid
    
    
    def sortedListToBST(self, head: ListNode) -> TreeNode: 
        """Recursive"""      
        if head is None:
            return None
        
        mid = self.get_mid(head)
        midnode = TreeNode(mid.val)
        if head == mid:
            return midnode

        midnode.left = self.sortedListToBST(head)
        midnode.right = self.sortedListToBST(mid.next)
        
        return midnode
        