# https://leetcode.com/problems/duplicate-zeros/submissions/

class Solution:
    def duplicateZeros(self, arr: List[int]) -> None:
        """
        Do not return anything, modify arr in-place instead.
        """
        possible_dups = 0  # how many duplicated zeros will be included in the avail space
        adj_len = len(arr)
        
        # First pass
        # First find the zeros and define how much space is needed from the end to accommodate...
        for left in range(len(arr)):
            if left >= adj_len - possible_dups:
                break
                
            if arr[left] == 0:
                # if left pointing to the last elem that can be included:
                # edge case: no more space for dupling this zero. Just keep the zero once and break
                if left == adj_len - 1 - possible_dups:
                    arr[adj_len - 1] = 0  # set it
                    adj_len -= 1  # the last one already handled (used for copying phase)
                    break  # Finished
                else:
                    possible_dups += 1
                    
        last = adj_len - 1 - possible_dups  # where to start the right to left traversal and copying
        
        # Second pass: Copy values
        # Copy values possible_dups steps right (decrease the possible dups on the way)
        for i in range(last, -1, -1):
            if arr[i] == 0:
                arr[i + possible_dups] = 0
                possible_dups -= 1
                arr[i + possible_dups] = 0
            else:
                arr[i + possible_dups] = arr[i]
                
        return arr
                    
        