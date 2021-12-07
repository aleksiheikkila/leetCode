# https://leetcode.com/problems/accounts-merge/

# adjacency matrix and dfs
# or Union find
# in this case, seems to be roughly comparable in speed


from collections import defaultdict

class UnionFind():
    def __init__(self, n: int):
        # at first, every node is in its own cluster, is its own parent / cluster representative
        self.parents = list(range(n))

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
        Just mindlessly assign the b be the new parent / cluster center of the union.
        """
        a_parent = self.find(a)
        b_parent = self.find(b)
        self.parents[a_parent] = b_parent

class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        N = len(accounts)
        uf = UnionFind(N)
        lookup = {}
        
        for idx, acc in enumerate(accounts):
            _, *emails = acc  # "rest"
            for email in emails:
                if email not in lookup:
                    # first encounter with this email
                    lookup[email] = idx  # email address to account index
                else:
                    # seen this email already, union the two accounts
                    uf.union(lookup[email], idx)
                    
        # collect all emails for a specific account
        acc_to_emails = defaultdict(set)  # account id to set of email addresses
        
        for idx, acc in enumerate(accounts):
            _, *emails = acc  # "rest"
            for email in emails:
                # add everything to the "cluster center account"
                acc_to_emails[uf.find(idx)].add(email)
                
        # construct result
        rst = []
        for i in range(N):
            # consider only those "cluster centers"
            if uf.find(i) == i:
                # [name, sorted_list_of_email_addrs]
                rst.append([accounts[i][0]] + sorted(acc_to_emails[i]))
                
        return rst


    def accountsMerge_dfs(self, accounts: List[List[str]]) -> List[List[str]]:
        email_to_name = {}
        # build adjacencies between email addresses
        # connect every email address to the first one in the same list
        adj_lists = defaultdict(set)

        for acc in accounts:
            name, *emails = acc
            for email in emails: #[1:]:  
                # need to start from zero to handle cases with just one email addr
                adj_lists[emails[0]].add(email)  
                adj_lists[email].add(emails[0])  # undirectional, having and element both ways
                email_to_name[email] = name

        # dfs to find the connected components
        visited = set()
        rst = []

        for email in adj_lists:  # iter thru keys
            if email in visited: 
                continue
            visited.add(email)
            stack = [email]
            emails = []

            while stack:
                curr_email = stack.pop()
                emails.append(curr_email)
                # add unvisited neighbors
                for neighbor_email in adj_lists[curr_email]:
                    if neighbor_email in visited: 
                        continue
                    visited.add(neighbor_email)
                    stack.append(neighbor_email)
            
            # stack empty for this account. Gather results
            rst.append([email_to_name[emails[0]]] + sorted(emails))

        return rst
