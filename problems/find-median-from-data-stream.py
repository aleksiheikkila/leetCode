# https://leetcode.com/problems/find-median-from-data-stream
# Hard

# Heaps, "data structure design"


"""
Implement the MedianFinder class (that supports streaming data):

MedianFinder() initializes the MedianFinder object.
void addNum(int num) adds the integer num from the data stream to the data structure.
double findMedian() returns the median of all elements so far. Answers within 10-5 of the actual answer will be accepted.
"""

from sortedcontainers import SortedList
from heapq import heappush, heappop


class MedianFinder:
    """ How to keep the data sorted?
    
    Split the data into two almost-equal size segments:
     - bottom: a max heap of the smaller values
     - top: a min heap (that is what python has implemented) of the larger values
     
    So that if the total number of nums is even, we take the largest value of the bottom
    (pop from maxheap) and the smallest value from the top (pop from minheap) and average these.
    
    If number of nums is odd, keep the data then so that the correct median value is in the bottom
    
    Stream: 1 6 2 1 7, 0
    -->
    bottom [0, 1, 1]
    top    [2, 6, 7]

    median (1+2)/2
    
    """ 
    def __init__(self):
        self.n = 0
        self.bottom = []
        self.top = []
        

    def addNum(self, num:int) -> None:
        """
        Steps:
        1. push new value to bottom heap
        2. pop from bottom (the largest value), push to top, 
        3. and if needed (if new length is odd), pop from top, push back to bottom
        
        This will ofc keep the heap conditions in bottom and top
        AND retain the condition that values in top >= values in bottom
        AND support a clear rule where the median is located.
        
        heappush and heappop have a runtime of O(log N).
        """
        # new size
        self.n += 1
        
        # python heaps are min heaps
        # bottom is max heap. Need to invert the numbers here and there
        heappush(self.bottom, -num)
        heappush(self.top, -heappop(self.bottom))
        if self.n % 2 != 0:
            heappush(self.bottom, -heappop(self.top))


    def findMedian(self) -> float:
        # two cases based on whether n is odd or even
        if self.n % 2 != 0:
            return -self.bottom[0]
        else:
            # average
            return 0.5*(self.top[0] - self.bottom[0])



class MedianFinder_SortedList:
    """Using SortedList, which would make this very easy (but is kind of cheating :)
    
    SortedList values are maintained in sorted order. .add() method to add a value
    """
    def __init__(self):
        self.lst = SortedList()
        self.n = 0


    def addNum(self, num: int) -> None:
        self.lst.add(num)
        self.n += 1
        

    def findMedian(self) -> float:
        # two cases based on whether n is odd or even
        if self.n % 2 != 0:
            return self.lst[self.n // 2]
        else:
            return 0.5*(self.lst[self.n//2 - 1] + self.lst[self.n//2])
        


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()
