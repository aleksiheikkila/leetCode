# https://leetcode.com/problems/min-stack

class MinStack:
    def __init__(self):
        """
        initialize your data structure here.
        """
        # stack contains tuples of (value, minimum value at or below this element in the stack)
        self.stack = []
        self.min_val = None
        

    def push(self, val: int) -> None:
        if self.min_val is None:
            # empty stack
            self.stack.append((val, val))  # value, minimum value at or below
            self.min_val  = val
        else:
            self.min_val = min(self.min_val, val)
            self.stack.append((val, self.min_val))
        

    def pop(self) -> None:
        self.stack.pop()                 
        self.min_val = None if len(self.stack) == 0 else self.top_minval()
    
    
    def top_minval(self) -> int:
        return self.stack[-1][1]

    
    def top(self) -> int:
        return self.stack[-1][0]
        

    def getMin(self) -> int:
        return self.min_val
        

# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()