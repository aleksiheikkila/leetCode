# https://leetcode.com/problems/maximum-number-of-eaten-apples

from queue import PriorityQueue
from heapq import heappush, heappop

class Solution:
    
    def eatenApples(self, apples: List[int], days: List[int]) -> int:
        assert len(apples) == len(days)

        h = []  # min heap. The "key" is the expiry day
        eaten, curr_day, num_days = 0, 0, len(apples)  

        while curr_day < num_days or h:
            # add apples if there are any, if within the apples array
            if curr_day < num_days and apples[curr_day] > 0:
                heappush(h, [curr_day + days[curr_day], apples[curr_day]])

            # remove rotten, or fully consumed
            while h and (h[0][0] <= curr_day or h[0][1] <= 0):
                heappop(h)

            # consume one apple if possible
            if h:
                # has something valid to consume after the previous step
                h[0][1] -= 1
                eaten += 1

            curr_day += 1

        return eaten


    def eatenApples_prioQueue(self, apples: List[int], days: List[int]) -> int:
        """ Slow priority queue based solution """
        assert len(apples) == len(days)
        
        eaten = 0
        q = PriorityQueue()
        
        for curr_day, (num_apples, days_to_expiry) in enumerate(zip(apples, days)):
            if num_apples > 0:
                q.put((curr_day + days_to_expiry, num_apples))
                
            # eat if possible                
            while not q.empty():
                expiration_day, apples_left = q.get()  # gives soonest / lowest expiry first
                if expiration_day <= curr_day or apples_left < 1:
                    continue
                # else eat and put back to the queue if there is something left
                eaten += 1
                if apples_left > 1:
                    q.put((expiration_day, apples_left - 1))
                break
            
        # after n days, we need to still keep on eating while we can
        curr_day += 1
        while not q.empty():
            expiration_day, apples_left = q.get()
            if expiration_day <= curr_day or apples_left < 1:
                continue
            # else eat and put back to the queue if there is something left
            eaten += 1
            curr_day += 1
            if apples_left > 1:
                q.put((expiration_day, apples_left - 1))

        return eaten
