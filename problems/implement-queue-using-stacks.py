# https://leetcode.com/problems/implement-queue-using-stacks

class MyQueue:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.stack = []
        self.helperstack = []  # for "rotating"
        

    def push(self, x: int) -> None:
        """
        Push element x to the back of queue.
        """
        
        # throw stack to helper
        while self.stack:
            self.helperstack.append(self.stack.pop())
        
        # add new
        self.stack.append(x)
        
        # throw helperstack back to stack
        while self.helperstack:
            self.stack.append(self.helperstack.pop())
        

    def pop(self) -> int:
        """
        Removes the element from in front of queue and returns that element.
        """
        return self.stack.pop()
        

    def peek(self) -> int:
        """
        Get the front element.
        """
        if not self.empty():
            return self.stack[-1]
        else:
            return None
        

    def empty(self) -> bool:
        """
        Returns whether the queue is empty.
        """
        return len(self.stack) == 0
        


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()