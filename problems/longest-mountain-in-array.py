# https://leetcode.com/problems/longest-mountain-in-array

# Fixes and workaround on top of another... became quite convoluted
# OK solution performance-wise, but could be made simpler

class Solution:
    def longestMountain(self, arr: List[int]) -> int:
        if len(arr) < 3:
            return 0
        
        max_len = 0
        N = len(arr)
        
        # lenght at least 3
        # stricly rising part, stricly falling part
        
        # find start of incr. part
        left = right = 1
        in_incr = False
        
        while left < N:
            if arr[left] > arr[left - 1]:
                # Found the start of increasing leg.
                in_incr = True
                right = left + 1
                
                while right < N:
                    if in_incr:
                        if arr[right] > arr[right - 1]:
                            pass
                        elif arr[right] == arr[right - 1]:
                            in_incr = False
                            break
                        else:
                            in_incr = False
                    else:
                        if arr[right] < arr[right - 1]:
                            pass
                        else:
                            # Started to increase again
                            subarr_len = (right - 1) - (left - 1) + 1
                            max_len = max(max_len, subarr_len)
                            break
                    
                    right += 1
                
                if right >= N:
                    break
                
                left = right - 1
                right = None
                
            left += 1
        
        if not in_incr and right is not None:
            max_len = max(max_len, right - left + 1)
        
        return max_len
        


    def longestMountain_simpler(self, A):
        N = len(A)
        ans = base = 0

        while base < N:
            end = base
            if end + 1 < N and A[end] < A[end + 1]: #if base is a left-boundary
                #set end to the peak of this potential mountain
                while end+1 < N and A[end] < A[end+1]:
                    end += 1

                if end + 1 < N and A[end] > A[end + 1]: #if end is really a peak..
                    #set 'end' to right-boundary of mountain
                    while end+1 < N and A[end] > A[end+1]:
                        end += 1
                    #record candidate answer
                    ans = max(ans, end - base + 1)

            base = max(end, base + 1)

        return ans