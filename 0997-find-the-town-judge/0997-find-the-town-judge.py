class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        if len(trust) == 0 and n == 1: return 1
        graph = defaultdict(list)
        for x , y in trust:
            graph[y].append(x)
        
        def dfs(node):
            if node in graph:
                for ne in graph[node]:
                    if ne not in seen:
                        seen.add(ne)
                        dfs(ne)
                    
        
        for k , v  in graph.items():
            seen = set()
            dfs(k)
            if len(v) == n-1 and k not in seen:
                return k

        return -1