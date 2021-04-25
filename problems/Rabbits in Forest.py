# https://leetcode.com/problems/rabbits-in-forest/

class Solution:
    def numRabbits(self, answers: List[int]) -> int:
        rabbits = 0
        peers = {}
        
        for ans in answers:
            if ans not in peers:
                rabbits += ans + 1
                if ans > 0:
                    peers[ans] = ans
            else:
                peers[ans] -= 1
                if peers[ans] == 0:
                    del peers[ans]
                
        return rabbits
        