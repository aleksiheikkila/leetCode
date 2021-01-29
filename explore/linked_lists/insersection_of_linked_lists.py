# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode_hash(self, headA: ListNode, headB: ListNode) -> ListNode:
        # first index where the two llists have the same node
        # hash table approach
        if headA is None or headB is None:
            return None
               
        nodes_A = set()
        node_a = headA
        node_b = headB
        while node_a is not None:
            nodes_A.add(node_a)
            node_a = node_a.next
            
        while node_b is not None:
            if node_b in nodes_A:
                return node_b
            node_b = node_b.next
            
        return None
            
            
        
        
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:
        # measure lengths, check that the last node is the same
        # then skip len_diff nodes from the longer llist and
        # step both llists to the first intersection
        if headA is None or headB is None:
            return None
        
        len_a = 1
        len_b = 1
        node_a = headA
        node_b = headB
        
        while node_a.next is not None:
            len_a += 1
            node_a = node_a.next
        while node_b.next is not None:
            len_b += 1
            node_b = node_b.next
        if node_a == node_b:
            # intersected, ended up to the same last node
            node_a = headA
            node_b = headB
            len_diff = abs(len_a - len_b)
            
            if len_a > len_b:
                for _ in range(len_diff):
                    node_a = node_a.next
            else:
                for _ in range(len_diff):
                    node_b = node_b.next
                    
            # then
            while node_a is not None and node_b is not None:
                if node_a == node_b:
                    return node_a
                else:
                    node_a = node_a.next
                    node_b = node_b.next
                
            
        return None 
    
    
    # There is also a two pointer approach that is comp: O(N), mem: O(1)