# https://leetcode.com/problems/count-good-meals

# Original version Relatively slow. New OK

class Solution:
    def countPairs(self, deliciousness: List[int]) -> int:
        from collections import Counter

        num_good_meals = 0
        
        POWERS_OF_TWO = [2**i for i in range(22)]
        counts = Counter(deliciousness)
        
        for d1, cnt1 in counts.items():
            for pwr2 in POWERS_OF_TWO:
                if pwr2 - d1 in counts and pwr2 - d1 <= d1:  
                    # avoid duplicates by limiting that the complement must not be larger
                    if pwr2 - d1 == d1:
                        num_good_meals += (counts[d1] * (counts[d1] - 1) // 2)
                        # combinations factorial formula reduces to the above
                    else:
                        num_good_meals += counts[pwr2-d1] * cnt1
            
        return int((num_good_meals) % (10**9 + 7))



    def countPairs2(self, deliciousness: List[int]) -> int:
        from collections import Counter
        from math import factorial as fac
        # power of two has only one 1-bit
        # num != 0 and (num & (num - 1) == 0)
        
        num_good_meals = 0
        
        POWERS_OF_TWO = [2**i for i in range(22)]
        counts = Counter(deliciousness)

        done = set()
        for d1, cnt1 in counts.items():
            for pwr2 in POWERS_OF_TWO:
                compl = pwr2 - d1
                if (min(d1,compl), max(d1, compl)) in done:
                    continue
                done.add((min(d1,compl), max(d1, compl)))
                n = counts[compl]                
                if n > 0:
                    if compl == d1:
                        if n > 1:
                            num_good_meals += (fac(n) / (fac(2) * fac(n-2)))
                    else:
                        num_good_meals += n*cnt1
      
        
        return int((num_good_meals) % (10**9 + 7))