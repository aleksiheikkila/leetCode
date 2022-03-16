class Node:
    def __init__(self, val, next=None):
        self.val = val
        self.next = next

class MyLinkedList:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.head = None
        self.len = 0
        
    def print(self):
        if self.head is not None:
            node = self.head
            print("LList content:")
            print(node.val, " -> ")
            while node.next is not None:
                node = node.next
                print(node.val, " -> ")
            print("##########")
        

    def get(self, index: int) -> int:
        """
        Get the value of the index-th node in the linked list. If the index is invalid, return -1.
        """
        
        if index > self.len - 1 or index < 0:
            return -1
        else:
            node = self.head
            for _ in range(index):
                node = node.next
                
            if node is None: 
                return -1
            else: 
                return node.val
        
        

    def addAtHead(self, val: int) -> None:
        """
        Add a node of value val before the first element of the linked list. After the insertion, the new node will be the first node of the linked list.
        """
        self.head = Node(val, self.head)
        self.len += 1

    def addAtTail(self, val: int) -> None:
        """
        Append a node of value val to the last element of the linked list.
        """
        if self.len == 0:
            self.addAtHead(val)  # increments len
        else:
            node = self.head
            while node.next is not None:
                node = node.next
            node.next = Node(val)
            self.len += 1
        

    def addAtIndex(self, index: int, val: int) -> None:
        """
        Add a node of value val BEFORE the index-th node in the linked list. If index equals to the length of linked list, the node will be appended to the end of linked list. If index is greater than the length, the node will not be inserted.
        """
        #print("AddAtIndex", index, self.len, "val:", val)
        #self.print()
        
        if index > self.len:
            return
        elif index == 0:
            self.addAtHead(val)
        elif index == self.len:
            self.addAtTail(val)
        else:
            node = self.head
            for _ in range(index-1):
                node = node.next  # insert after node
            new_node = Node(val, next=node.next)
            node.next = new_node
            self.len += 1


    def deleteAtIndex(self, index: int) -> None:
        """
        Delete the index-th node in the linked list, if the index is valid.
        """  
        if index >= self.len or index < 0:
            return
        elif index == 0:
            self.head = self.head.next
        else:  
            prev_node = self.head
            for _ in range(index - 1):
                prev_node = prev_node.next
            prev_node.next = prev_node.next.next if prev_node.next is not None else None
        
        self.len -= 1


# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)