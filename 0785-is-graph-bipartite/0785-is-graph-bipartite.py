class Solution:
    def isBipartite(self, graph: List[List[int]]) -> bool:
        
        def dfs(node):
            res = True
            for n in graph[node]:
                if color[n] == -1:
                    if color[node] == 0:
                        color[n] = 1
                    else:
                        color[n] = 0
                    res = res and dfs(n)
                elif color[n] == color[node]:
                    return False
            
            return res

        color = [-1] * len(graph)

        for node in range(len(graph)):
            if  color[node] == -1:
                color[node] = 0
                if not dfs(node):
                    return False
        return True
