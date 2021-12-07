# https://leetcode.com/problems/all-paths-from-source-to-target

class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        # DFS, backtracking
        # BFS allows early stopping for shortest path probs... we are not after that
        # DFS will have here clearly better space complexity
        
        paths = []
        N = len(graph)
        
        def backtrack(cand: list[int]) -> None:
            # check if candidate is valid: ends to the last node?
            if cand[-1] == N - 1:
                paths.append(cand.copy())
            else:
                # where can we go from the current node?
                # explore all, backtrack
                # DAG: ensures no loops
                for next_node in graph[cand[-1]]:
                    cand.append(next_node)
                    backtrack(cand)
                    cand.pop()  # backtrack, remove the one we added
        
        # start from the first node:
        backtrack([0])
        return paths
    