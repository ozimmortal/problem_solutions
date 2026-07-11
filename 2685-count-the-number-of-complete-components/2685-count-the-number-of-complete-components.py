class UF:
    def __init__(self, n):
        self.parent = [i for i in range(n)]
        self.size = [1] * n
    
    def find(self , x):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]
    
    def union(self, x, y):
        px, py = self.find(x), self.find(y)
        if px == py: return
        if self.size[px] < self.size[py]:
            px, py = py, px
        self.parent[py] = px
        self.size[px] += self.size[py]
    


class Solution:
    def countCompleteComponents(self, n: int, edges: List[List[int]]) -> int:
        
        graph = defaultdict(list)
        uf = UF(n)
        for x ,y in edges:
            uf.union(x , y)
            graph[x].append(y)
            graph[y].append(x)
        

        def dfs(node , seen):
            nonlocal cnt
            for vert in graph[node]:
                cnt +=  1
                if vert not in seen:
                    seen.add(vert)
                    dfs(vert, seen) 
        
        parents = Counter(uf.find(i) for i in range(n))
        conn = 0
        for p in parents:
            k = parents[p]
            cnt = 0
            if k <= 2 :
                conn += 1
            else:
                dfs(p , {p})
                if (cnt//2) == (k * (k - 1)) / 2:
                    conn +=1
        
        return conn



