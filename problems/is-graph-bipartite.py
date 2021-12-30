# https://leetcode.com/problems/is-graph-bipartite
# Medium

# Graph, DFS

"""
A graph is bipartite if the nodes can be partitioned into two independent sets A and B 
such that every edge in the graph connects a node in set A and a node in set B.

So there is no edges between nodes of partition A
And no edged between nodes of partition B


Approach:
dfs

assign the starting node to group 0.

as we go, assign unassigned neighbors to the opposite group.
for already assigned nodes, check that they are in the different group
So do the checks at adjs processing time.

start from all nodes to cover possibly isolated parts of the graph
"""

from collections import List


class Solution:
    def isBipartite(self, graph: List[List[int]]) -> bool:
        
        group_membership = dict()  # node -> group [0 or 1]
        
        stack = []
        # start from each node
        for starting_node in range(len(graph)):
            if starting_node in group_membership:
                continue
                
            # else it's a new, unvisited starting point
            group_membership[starting_node] = 0
            stack.append(starting_node)
            
            while stack:
                node = stack.pop()
                group = group_membership[node]
            
                for adj_node in graph[node]:
                    if adj_node not in group_membership:
                        # unassigned neigh: add to the different group, add to the stack
                        group_membership[adj_node] = 1 - group
                        stack.append(adj_node)
                    elif group_membership[adj_node] == group:
                        return False
        
        # no violations found: graph is bipartite!    
        return True
        