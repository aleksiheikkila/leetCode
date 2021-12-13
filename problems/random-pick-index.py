# https://leetcode.com/problems/random-pick-index

from random import choice
from collections import defaultdict
from typing import List

class Solution:

    def __init__(self, nums: List[int]):
        self.num_to_indices = defaultdict(list)
        for idx, num in enumerate(nums):
            self.num_to_indices[num].append(idx)
        

    def pick(self, target: int) -> int:
        return choice(self.num_to_indices[target])
        


# Your Solution object will be instantiated and called as such:
# obj = Solution(nums)
# param_1 = obj.pick(target)