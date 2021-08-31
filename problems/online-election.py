# https://leetcode.com/problems/online-election

from collections import Counter
from bisect import bisect


class TopVotedCandidate:

    def __init__(self, persons: List[int], times: List[int]):
        self.leader_ts = []  # logs timestamps when leader changes (time, new leader tuples)
        
        counts = Counter()
        leader, max_votes = None, 0
        
        # already sorted
        for person, t in zip(persons, times):
            counts[person] += 1  # defaultdict(int) like
            c = counts[person]
            
            if c >= max_votes:  # if tied, keep the most recent
                if person != leader:
                    leader = person
                    self.leader_ts.append((t, leader))
                    
                max_votes = c              
    

    def q(self, t: int) -> int:
        idx = bisect(self.leader_ts, (t, float("inf")))   
        # returns the index to the right. So idx is the index where the time is "next higher from t"
        # bisect compares tuples. it first checks the first element, then the second
        # so (2,1) > (1, 9999) and (1, 5) < (1, 6) etc
        
        if idx == 0:
            # In this case, we are asking for the leader at time when no votes are cast!
            return None
        else:
            return self.leader_ts[idx - 1][1]
                    
                     

class TopVotedCandidate_tooSlow:
    # TOO SLOW, DOES NOT PASS

    def __init__(self, persons: List[int], times: List[int]):
        # already sorted
        self.times = times
        self.persons = persons
        
        #self.times, self.persons = (list(l) 
        #                            for l in zip(*sorted(zip(times, persons))))
        
    def get_next_larger_time_idx(self, t: int) -> int:
        # boundary
        left, right = 0, len(self.times) - 1
        next_larger_time_idx = 0
        
        while left <= right:
            mid = left + (right - left) // 2
            
            if self.times[mid] > t:
                right = mid - 1
            else:
                left = mid + 1
                
        return max(left, mid)
        

    def q(self, t: int) -> int:
        next_time_idx = self.get_next_larger_time_idx(t)
        #print("next time idx:", next_time_idx)

        counts = Counter(self.persons[:next_time_idx])
        max_votes = None
        potential_winners = set()
        for candidate, votes in counts.most_common():
            if max_votes is None:
                max_votes = votes
                potential_winners.add(candidate)
            elif votes < max_votes:
                break
            else:
                potential_winners.add(candidate)
        
        if len(potential_winners) == 1:
            return list(potential_winners)[0]
        
        # else find the most recent
        for p in reversed(self.persons[:next_time_idx]):
            if p in potential_winners:
                return p
            


# Your TopVotedCandidate object will be instantiated and called as such:
# obj = TopVotedCandidate(persons, times)
# param_1 = obj.q(t)