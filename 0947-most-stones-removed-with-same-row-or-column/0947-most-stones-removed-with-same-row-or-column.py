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
            return
        if self.size[rx] < self.size[ry]:
            rx, ry = ry, rx
        self.parent[ry]  = rx
        self.size[rx]   += self.size[ry]
        self.counts -= 1

class Solution:
    def removeStones(self, stones: List[List[int]]) -> int:
        n = len(stones)
        graph = defaultdict(list)
        for i in range(n):
            x , y = stones[i]
            for j in range(i + 1 , n):
                x2 , y2 = stones[j]
                if x2 == x or y2 == y:
                    graph[i].append(j)
                    graph[j].append(i)
        print(graph)
        uf = UF(n)
        for k in graph:
            for v in graph[k]:
                uf.union(k , v)
        
        print(uf.parent)
        return n - uf.counts 
        