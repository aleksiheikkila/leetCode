# https://leetcode.com/problems/swim-in-rising-water
# Hard
# Connected components
# Union Find problem

class UnionFind():
    def __init__(self):
        # construc dynamically
        self.parents = {}  # key to parent
        self.sizes = {}  # key (cluster repres.) to cluster size

    def __contains__(self, x):
        return x in self.parents

        
    def insert(self, x) -> None:
        if x in self.parents: return
        self.parents[x] = x
        self.sizes[x] = 1
        
    def find(self, x: int) -> int:
        """Find the cluster representive for node x"""
        while x != self.parents[x]:
            # not yet at the cluster representative
            self.parents[x] = self.find(self.parents[x])  # path compression
            x = self.parents[x]
        return x

    def union(self, a: int, b: int) -> None:
        """
        Union the two subsegments together.
        """
        a_parent = self.find(a)
        b_parent = self.find(b)
        if a_parent == b_parent: return
        
        small, big = sorted([a_parent, b_parent], key=lambda x: self.sizes[x])
        self.parents[small] = big
        self.sizes[big] += self.sizes[small]
        # need to get rid of sizes[small]?

class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        N = len(grid)
        uf = UnionFind()
        t_to_loc = {grid[r][c]: (r,c) for r in range(N) for c in range(N)}  # unique vals
        
        for t in range(N**2):
            r, c = t_to_loc[t]
            uf.insert((r,c))
            for r2, c2 in ((r+1, c), (r-1, c), (r, c+1), (r, c-1)):
                if (r2, c2) in uf:
                    # adjacent is already submerged, connect
                    uf.union((r,c), (r2, c2))
                    
            if (0,0) in uf and (N-1, N-1) in uf and uf.find((0,0)) == uf.find((N-1, N-1)):
                return t
        
        
        