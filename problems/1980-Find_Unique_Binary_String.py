"""
    1980. Find Unique Binary String
    Medium

    Given an array of strings nums containing n unique binary strings each of length n, return a binary string of length n that does not appear in nums. 
    If there are multiple answers, you may return any of them.
"""

from typing import List


def genbins(n: int, bs: str = '') -> str:
    """Generator for all binary strings of lenght n"""
    if n == 0:
        yield bs
    else:
        yield from genbins(n - 1, bs + '0')
        yield from genbins(n - 1, bs + '1')

        
class Solution:
    def findDifferentBinaryString1(self, nums: List[str]) -> str:
        strs_set = set(nums)

        for bin_str in genbins(len(nums)):
            if bin_str not in strs_set:
                return bin_str

    def findDifferentBinaryString2(self, nums: List[str]) -> str:
        # use numbers

        # strings as ints in a set
        nbrs = set([int(num, 2) for num in nums])

        num_bits = len(nums[0])
        max_number = 2 ** num_bits 

        for nbr in range(max_number):
            if nbr not in nbrs:
                # return the string
                # lpad to the num bits
                return format(nbr, f"0{num_bits}b")
            
    def findDifferentBinaryString3(self, nums: List[str]) -> str:
        """
        We are given that number of bits in the number is equal to number of elements (n unique binary strings each of length n)


        Create a binary string which differs from first binary at 1st position, second binary at 2nd position, third binary at 3rd position, ...
        This will make sure that the binary we have made is unique (as it differs from all others at at least one position).

        """

        selected_bin_chars = []

        for i, num in enumerate(nums):
            selected_bin_chars.append(
                "0" if num[i] == "1" else "1"
            )

        return "".join(selected_bin_chars)
