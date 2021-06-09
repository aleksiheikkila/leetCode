# https://leetcode.com/problems/lfu-cache/

from collections import OrderedDict, defaultdict

class Node:
    # For single cache elements
    def __init__(self, val, count=1):
        self.val = val
        self.count = count

class LFUCache:
    """
    Uses to datastructures.
        * cache is a dict: key -> node
        * countbuckets: {count[int] -> OrderedDict {key: Node}}, for handling the LFU bookkeeping

    """
    def __init__(self, capacity: int):
        assert capacity >= 0
        self.capacity = capacity
        self.minCount = 0
        self.cache = {}  # key: Node(val, count)

        self.countbuckets = defaultdict(OrderedDict) 
        # count: OrderedDict(key: Node(val, count))
        

    def get(self, key: int) -> int:
        if key not in self.cache:
            return -1
        
        #  else get value and update count
        node = self.cache[key]
        # move the node to the next countbucket (ordereddict, so becomes most recent there)
        del self.countbuckets[node.count][key]
        node.count += 1
        self.countbuckets[node.count][key] = node
        
        # if the mincount bucket is empty, increase the mincount
        if len(self.countbuckets[self.minCount]) == 0:
            del self.countbuckets[self.minCount]
            self.minCount += 1
        
        return node.val
        

    def put(self, key: int, value: int) -> None:
        if self.capacity <= 0:
            return
        
        if key in self.cache:
            self.cache[key].val = value
            self.get(key)  # this handles the count updating
            return
        
        # if key not in cache, add
        # if at max capacity, first remove the LFU node
        if len(self.cache) == self.capacity:
            LFUKey, _ = self.countbuckets[self.minCount].popitem(last=False)  # least recent
            if len(self.countbuckets[self.minCount]) == 0:
                del self.countbuckets[self.minCount]
            
            del self.cache[LFUKey]
            
        # create new node and add to cache
        newNode = Node(val=value)
        self.cache[key] = newNode
        self.countbuckets[1][key] = newNode
        self.minCount = 1
        

# Your LFUCache object will be instantiated and called as such:
# obj = LFUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)