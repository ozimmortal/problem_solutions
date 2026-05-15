class Solution:
    def getAncestors(self, n: int, edges: List[List[int]]) -> List[List[int]]:

        ans = [[] for _ in range(n)]
        graph = defaultdict(list)

        for x , y in edges:
            graph[y].append(x)
        
        def dfs(i):
            for n in graph[i]:
                if n not in seen:
                    seen.add(n)
                    a.append(n)
                    dfs(n)

        for i in range(n):
            if i in graph:
                a = []
                seen = {i}
                dfs(i)
                ans[i] = sorted(a)

       
        return ans

                
