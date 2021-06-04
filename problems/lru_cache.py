# https://leetcode.com/problems/lru-cache

# Using OrderedDict

from collections import OrderedDict

class LRUCache:

    def __init__(self, capacity: int):
        assert capacity > 0
        self.capacity = capacity
        self.cache = OrderedDict()
        # last element is the most recent. First element is the oldest
        

    def get(self, key: int) -> int:
        if key not in self.cache:
            return -1
    
        # else, get val and move to the end (make it most recent)  
        value = self.cache[key]
        self.cache.move_to_end(key)
        
        return value
        

    def put(self, key: int, value: int) -> None:
        self.cache[key] = value
        
        # move to end
        self.cache.move_to_end(key)
        # remove first element (least recent) if went over capacity
        if len(self.cache) > self.capacity:
            self.cache.popitem(last=False)
        

# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)