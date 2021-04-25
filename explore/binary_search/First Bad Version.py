# https://leetcode.com/explore/learn/card/binary-search/126/template-ii/947/

# The isBadVersion API is already defined for you.
# @param version, an integer
# @return an integer
# def isBadVersion(version):

class Solution:
    def firstBadVersion(self, n):
        """
        :type n: int. Number of versions: 1, 2, ..., n
        :rtype: int
        """
        left, right = 1, n
        
        while left <= right:
            # mid = (left + right) // 2
            # in some languages, this could overflow
            # use overflow-safe version instead:
            mid = left + ((right - left) // 2)
            
            if isBadVersion(mid):
                right = mid - 1
            else:
                left = mid + 1
                
        return left
                