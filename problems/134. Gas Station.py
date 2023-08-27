""" 
134. Gas Station
Medium
https://leetcode.com/problems/gas-station/

There are n gas stations along a circular route, where the amount of gas at the ith station is gas[i].

You have a car with an unlimited gas tank and it costs cost[i] of gas to travel from the ith station to 
its next (i + 1)th station. You begin the journey with an empty tank at one of the gas stations.

Given two integer arrays gas and cost, return the starting gas station's index if you can travel around 
the circuit once in the clockwise direction, otherwise return -1. If there exists a solution, it is guaranteed to be unique
"""

from typing import List

class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        """
        This is a greedy problem
        
        if sum(gas) >= sum(cost) --> there is a solution
        And only one unique solution, as stated in the prob.

        Otherwise not.
        """
        
        if sum(gas) < sum(cost):
            return -1
        
        # else there is a solution, and only one
        total = start = 0
        for i in range(len(gas)):
            total += (gas[i] - cost[i])
            if total < 0:
                total = 0
                start = i + 1
                
        """ Why need to go through this only once?
        if starting at some earlier positions did not work out --> those could not be the solution
        if we get from pos i to the end, we know that must be the unique sol
        (because of uniqueness, the solution wont be starting at later pos i + x).

        Why no need to restart from the next starting pos?
        Because that won't work 
        (starting from empty tank at a position where we already drove past with >= empty tank and failed to make the lap...)
        """
                
        return start
