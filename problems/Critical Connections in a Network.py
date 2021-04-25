# https://leetcode.com/explore/challenge/card/april-leetcoding-challenge-2021/596/week-4-april-22nd-april-28th/3719/

# Tarjan's algo
# O(V+E)

class Solution:
    
    def dfs(self, u, disc, low, parent, bridges):
        # Tarjan's single pass
        disc[u] = low[u] = self.time
        self.time += 1
        
        for v in self.adjs[u]:
            if disc[v] == -1:  # not visited
                parent[v] = u
                self.dfs(v, disc, low, parent, bridges)
                # when backtracks:
                low[u] = min(low[u], low[v])
                
                if low[v] > disc[u]:
                    # found a bridge
                    bridges.append([u, v])
            
            elif parent[u] != v:  # already visited. Ignore child - parent edge (removed)
                # Already visited, not the parent.
                low[u] = min(low[u], disc[v])
        
    
    def findBridges(self):
        # UNSEEN = -1
        disc = [-1 for _ in range(self.n)]
        low = [-1 for _ in range(self.n)]
        parent = [-1 for _ in range(self.n)]
        bridges = []
        
        for i in range(self.n):
            if disc[i] == -1 :
                self.dfs(i, disc, low, parent, bridges)
                
        return bridges
    
    
    def criticalConnections(self, n: int, connections: List[List[int]]) -> List[List[int]]:

        # A critical connection is a connection that, if removed, 
        # will make some server unable to reach some other server.
        
        # Bridge: an edge, if removed, increases the number of components in a graph
        # A component of an undirected graph is an induced subgraph in which any two vertices 
        # are connected to each other by paths, and which is connected to no additional vertices 
        # in the rest of the graph
        
        # Bridges are the critical connections (single point of failures)
        # Remove an edge (only one at a time). If number of components increase, 
        # it was a critical component

        self.time = 0
        self.n = n
        self.adjs = [[] for _ in range(n)]
        for orig, dest in connections:
            assert orig != dest
            self.adjs[orig].append(dest)
            self.adjs[dest].append(orig)
            
        return self.findBridges()
    