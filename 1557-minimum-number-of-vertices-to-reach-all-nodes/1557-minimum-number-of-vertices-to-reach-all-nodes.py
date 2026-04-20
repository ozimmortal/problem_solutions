class Solution:
    def findSmallestSetOfVertices(self, n: int, edges: List[List[int]]) -> List[int]:

        seen = set()
        graph = defaultdict(list)
        for f , t in edges:
            graph[f].append(t)

        def dfs(node):

            for n in graph[node]:

                if n not in seen:
                    seen.add(n)
                    dfs(n)
        
        res = []
        for i in range(n):
            dfs(i)
        
        for i in range(n):
            if i not in seen:
                res.append(i)
        
        return res