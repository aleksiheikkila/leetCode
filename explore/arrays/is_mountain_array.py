# https://leetcode.com/explore/learn/card/fun-with-arrays/527/searching-for-items-in-an-array/3251/

# pretty ugly 
class Solution:
    def validMountainArray_old(self, arr: List[int]) -> bool:
        if arr is None or len(arr) < 3:
            return False
        
        incr_stage = True  # false: decreasing stage
        
        i=1
        while i < len(arr):
            if arr[i] > arr[i-1]:
                if not incr_stage:
                    return False
            elif arr[i] < arr[i-1]:
                if incr_stage:
                    if i == 1:  # there was no increasing part, not a mountain
                        return False
                    incr_stage = False
            else:  # same value
                return False
            
            i += 1
            
        return not incr_stage


    # better version
    def validMountainArray(self, arr: List[int]) -> bool:
        N = len(arr)
        i = 0

        # find the top
        while i+1 < N and arr[i] < arr[i+1]:
            i += 1
        
        # top cannot be first nor last
        if i == 0 or i == N-1:
            return False

        # walk down
        while i+1 < N and arr[i] > arr[i+1]:
            i += 1

        return i == N - 1
