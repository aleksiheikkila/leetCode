# Definition for singly-linked list.
#class ListNode:
#    def __init__(self, x):
#        self.val = x
#        self.next = None

class Solution:
    def hasCycle(self, head: ListNode) -> bool:
        # kind of Floyd's cycle-finding algo
        # Floyd’s Cycle-Finding Algorithm uses two pointers that move at different speeds. 
        # If there is a cycle, both of the pointers would point to the same value at some point in the future.
        
        if head is None:
            return False
        
        slow = head
        fast = head.next
        while slow != fast:
            if fast is None or fast.next is None:
                return False
            slow = slow.next
            fast = fast.next.next
        
        return True
        
        
    def detectCycle(self, head: ListNode) -> ListNode:
        # Returns the node where the cycle starts (or None if no cycle)
        
        # If list is empty or has only one node --> no loops
        if (head == None or head.next == None):
            return None
        
        slow = head.next
        fast = head.next.next

        # Move slow and fast 1 and 2 steps
        # ahead respectively.

        # Search for a loop using slow an fast pointers
        while (fast and fast.next):
            if (slow == fast):
                break

            slow = slow.next
            fast = fast.next.next  # both step at the same time, before comparing

        # If loop does not exist. If linked list ends to next=None, there is no loop
        if (slow != fast):  # came to end
            return None

        # If loop exists. Start slow from
        # head and fast from meeting point.
        # both have step size of 1
        slow = head

        while (slow != fast):
            slow = slow.next
            fast = fast.next

        return slow
        