# https://leetcode.com/problems/minimum-window-substring/

"""We keep expanding the window by moving the right pointer. 
When the window has all the desired characters, we contract (if possible) 
and save the smallest window till now.
"""

# Accepted but quite slow
# Optimizations
# Check the effect of adding/removing one char in more efficient way 
# instead of comparing whole array

# create a filtered s, with only chars that are in t present (as tuples, with index)
# and traverse that

class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(s) < len(t):
            return ""
            
        min_left = min_right = None
        min_len = float("inf")
        ord_A = ord("A")

        t_counts = [0] * (ord("z") - ord("A") + 1)
        window_counts = [0] * (ord("z") - ord("A") + 1)

        for c in t:
            t_counts[ord(c) - ord_A] += 1

        #print("t counts:", t_counts)

        def includes_all_chars(chars: list, needed: list):
            """list"""
            return all(chars[idx] >= need for idx, need in enumerate(needed))

        #def can_remove(chars: list, needed: list, remove_char):
        #    """list"""
        #    chars[ord(remove_char) - ord_A] -= 1
        #    can_remove = all(chars[idx] >= need for idx, need in enumerate(needed))
        #    chars[ord(remove_char) - ord_A] += 1
        #    return can_remove

        window_len = 0
        left = right = 0
        while right < len(t):
            window_counts[ord(s[right]) - ord_A] += 1
            right += 1
            window_len += 1

        if window_counts == t_counts:
            return s[:right]

        # sliding window
        # keep expanding to right as long as does not contain all chars
        while right < len(s):
            while includes_all_chars(window_counts, t_counts):
                if window_len < min_len:   
                    # new minimum
                    min_len = window_len
                    min_left, min_right = left, right
                    #print("new min len:", min_len, min_left, min_right)

                    # if smallest possible, quit early
                    if window_len == len(t):
                        return s[min_left:min_right]

                # if window has extra chars
                if window_len > len(t):
                    # TODO: COuld get rid of the can_remove logic. Yes, it can be removed.
                    window_counts[ord(s[left]) - ord_A] -= 1
                    window_len -= 1
                    left += 1
                else:
                    break

                # Do not make it not to includ all...

            # expand to right
            window_counts[ord(s[right]) - ord_A] += 1
            window_len += 1
            right += 1

        # Finally prune as much from left as possible
        while includes_all_chars(window_counts, t_counts):
                if window_len < min_len:
                    min_len = window_len
                    min_left, min_right = left, right

                window_counts[ord(s[left]) - ord_A] -= 1
                window_len -= 1
                left += 1

        if min_left is None:
            return ""
        else:
            return s[min_left:min_right]
                