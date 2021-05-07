# https://leetcode.com/explore/challenge/card/april-leetcoding-challenge-2021/597/week-5-april-29th-april-30th/3726/

from math import log

class Solution:
    def powerfulIntegers(self, x: int, y: int, bound: int) -> List[int]:
        rst = set()
        if bound < 2:
            return list(rst)
        
        max_exp_x = round(log(bound - 1, x)) if x > 1 else 0
        max_exp_y = round(log(bound - 1, y)) if y > 1 else 0
        # needed to put round, likely due to rounding errors / lack of precision
        # 1**a is always 1
        
        for exp_x in range(max_exp_x + 1):
            for exp_y in range(max_exp_y + 1):
                powerful = x**exp_x + y**exp_y
                if powerful <= bound:
                    rst.add(powerful)
                else:
                    break
                    
        return list(rst)