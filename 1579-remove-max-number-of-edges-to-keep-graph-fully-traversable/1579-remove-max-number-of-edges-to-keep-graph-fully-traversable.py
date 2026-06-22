class UF:
    def __init__(self, n):
        self.parent = list(range(n))
        self.size   = [1] * n
        self.counts = n

    def find(self, x):
        while self.parent[x] != x:
            self.parent[x] = self.parent[self.parent[x]]  
            x = self.parent[x]
        return x

    def union(self, x, y):
        rx, ry = self.find(x), self.find(y)
        if rx == ry:
            return 0
        if self.size[rx] < self.size[ry]:
            rx, ry = ry, rx
        self.parent[ry]  = rx
        self.size[rx]   += self.size[ry]
        self.counts -= 1
        return 1

    def isConnected(self):
        return self.counts == 2

class Solution:
    def maxNumEdgesToRemove(self, n: int, edges: List[List[int]]) -> int:

        alice , bob = UF(n + 1), UF(n + 1)
        count = 0
        
        for t , s , e in edges:
            if t == 3:
                count += (alice.union(s , e) | bob.union(s , e))
        
        for t , s , e in edges:

            if t == 1:
                count += alice.union(s ,e)
            elif t == 2:
                count += bob.union(s , e)

        if alice.isConnected() and bob.isConnected():
            return len(edges) - count
        return -1

        