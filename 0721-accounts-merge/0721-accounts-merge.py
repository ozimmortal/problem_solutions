class UF:
    def __init__(self, n):
        self.parent = list(range(n))
        self.size   = [1] * n

    def find(self, x):
        while self.parent[x] != x:
            self.parent[x] = self.parent[self.parent[x]]  
            x = self.parent[x]
        return x

    def union(self, x, y):
        rx, ry = self.find(x), self.find(y)
        if rx == ry:
            return
        if self.size[rx] < self.size[ry]:
            rx, ry = ry, rx
        self.parent[ry]  = rx
        self.size[rx]   += self.size[ry]

class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:

        n = len(accounts)
        uf = UF(n)
        graph = defaultdict(int)

        for i in range(n):
            emails = accounts[i][1:]
            for email in emails:    
                if email in graph:
                    uf.union(graph[email], i)
                graph[email] = uf.find(i)
        
        res = {}
        for i in range(n):
            x = uf.find(i)
            account = accounts[i]
            
            if x in res:
                res[x] = res[x].union(set(account[1:]))
            else:
                res[x] = set(account[1:])

        return [[accounts[k][0]] + sorted(list(res[k])) for k in res]
        
        

        
        




        