# https://leetcode.com/problems/implement-stack-using-queues
from collections import deque

# Could have used also from queue import Queue
# I was then wondering how to implement the top() in some easy and efficient way
# It occured to me later that one can call .queue for the queue object
# that gives a deque where one can index into... so the top would become just like
# return q.queue[0]

class MyStack:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.q1 = deque()
        self.q2 = deque()
        # I will be adding to the right and popping from the left
        # So the queing happens from right to left.
        self.sz = 0
        

    def push(self, x: int) -> None:
        """
        Push element x onto stack.
        """
        # Empty, put new item to the front, add existing ones back in the same order they were
        # NO NEED TO EMPTY FIRST: SwITCH THE QUEUES INSTEAD 
        
        # NOT NEEDED:
        #for _ in range(self.sz):
        #   self.q2.append(self.q1.popleft())
            
        # start with the empty queue (queue pointed by q2 is always empty at this point)
        self.q2.append(x)
        
        # Add the existing ones in the same order
        for _ in range(self.sz):
            self.q2.append(self.q1.popleft())    
        
        self.sz += 1
        
        # Switch the q1 and q2 so that q2 again points to the empty one
        self.q1, self.q2 = self.q2, self.q1
        

    def pop(self) -> int:
        """
        Removes the element on top of the stack and returns that element.
        """
        if self.sz > 0:
            self.sz -= 1
            return self.q1.popleft()
        else:
            return None
        

    def top(self) -> int:
        """
        Get the top element.
        i.e. self.q1
        """
        return self.q1[0] if self.sz > 0 else None
        

    def empty(self) -> bool:
        """
        Returns whether the stack is empty.
        """
        return self.sz == 0
        


# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()