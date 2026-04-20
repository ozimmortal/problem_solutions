class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        
        graph = defaultdict(list)
        for x ,y in edges:
            graph[x].append(y)
            graph[y].append(x)
        
        def dfs(node):
            for n in graph[node]:
                if n not in seen:
                    seen.add(n)
                    dfs(n)
        
        ans = 0
        seen = set()
        for i in range(n):
            if i not in seen:
                seen.add(i)
                dfs(i)
                ans += 1
        
        return ans
            