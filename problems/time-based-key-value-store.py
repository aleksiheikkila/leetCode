# https://leetcode.com/problems/time-based-key-value-store

from collections import defaultdict
import bisect

class TimeMap:
    """Performance is good"""

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.timestamps = defaultdict(list)
        self.values = defaultdict(list)


    def set(self, key: str, value: str, timestamp: int) -> None:
        self.timestamps[key].append(timestamp)  # stricty increasing
        self.values[key].append(value)


    def get(self, key: str, timestamp: int) -> str:
        # bisect-based
        correct_idx = bisect.bisect(self.timestamps[key], timestamp) - 1
        # bisect will returns where the timestamp needs to go to keep timestamps in sorted order
        # so the prev value smaller than or equal ti timestamp is the one before that
        # Corner case: when bisect returns index 0, there is not such value!
        return self.values[key][correct_idx] if correct_idx >= 0 else ""

        


class TimeMap_slow:
    """This is quite inefficient"""

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.store = defaultdict(list)  # key -> list [(ts_from, ts_to, val)]

    def set(self, key: str, value: str, timestamp: int) -> None:
        if len(self.store[key]) > 0:
            self.store[key][-1][1] = timestamp
        self.store[key].append([timestamp, float("inf"), value])


    def get(self, key: str, timestamp: int) -> str:
        # naive, slow
        
        if key not in self.store:
            return ""
        
        elem_list = self.store[key]
        if elem_list[0][0] > timestamp:
            return ""

        left, right = 0, len(elem_list) - 1
        while left <= right:
            mid = (left + right) // 2
            if elem_list[mid][0] <= timestamp and elem_list[mid][1] > timestamp:
                return elem_list[mid][2]
            
            if elem_list[mid][0] > timestamp:
                right = mid - 1
            else:
                left = mid + 1


            
        
                
        

# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)