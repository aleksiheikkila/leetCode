# https://leetcode.com/problems/prison-cells-after-n-days

class Solution:
    def prisonAfterNDays_naive(self, cells: List[int], n: int) -> List[int]:
        """Inefficient version that times out.
        Just naively repeat the update rule"""
        
        def get_next_state(state: List[int]):
            """ Given current cells state, generate the next state.
            Rule:
            If cell has two adj neighbors and they are both in same state
            Then cell becomes occupied (i.e. set to value 1)
            First and last cell does not have two neighbors -> they become and stay zero
            """
            # zip stops when the shortest list ends
            return [0] + [int(prev == nxt) for prev, nxt in zip(state, state[2:])] + [0]
        
        state = cells.copy()
        for _ in range(n):
            state = get_next_state(state)
            
        return state

"""
Notice that cells/state can have 2**8 = 256 different states.
if n is very large, we will see same states repeatedly.

Notice also that the update rule is fully deterministic and depends only on the state.
The same state leads to same subsequent states every time

Thus, with large n > 256 there will be cycles. We can utilize this to skip a lot of stes
"""


class Solution:
    def prisonAfterNDays(self, cells: List[int], n: int) -> List[int]:
        
        def get_next_state(state):
            """
            Rules. 
            If cell has two adj neighbors and they are both in same state
            Then cell becomes occupied (i.e. set to value 1)
            First and last cell does not have two neighbors -> they become and stay zero
            """
            # zip stops when the shortest list ends
            return tuple([0] + [int(prev == nxt) for prev, nxt in zip(state, state[2:])] + [0])
        

        state = tuple(cells)
        state_to_step = dict()  # tuple of state as key, step_num when it was seen as value
        
        for step_num in range(n):
            if state not in state_to_step:
                state_to_step[state] = step_num
                state = get_next_state(state)
            else:
                # Cycle found!
                cycle_len = step_num - state_to_step[state]
                steps_left = n - step_num
                break       
        # if loop completed normally, i.e. we did not break out / find a cycle. Return state
        else: 
            return list(state)
        
        # Else utilize the cycle length and just loop the last x steps (x < 64)
        for _ in range(steps_left % cycle_len): 
            state = get_next_state(state)
            
        return list(state)
    