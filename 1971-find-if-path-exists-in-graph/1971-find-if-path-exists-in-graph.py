class Solution:
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        
        graph= defaultdict(list)
        for x ,y in edges:
            graph[x].append(y)
            graph[y].append(x)
        
        def dfs(node):
            if node == destination:
                self.reached = True
                return

            for n in graph[node]:
                if n not in seen:
                    seen.add(n)
                    dfs(n)


        self.reached = False
        seen = {source}
        dfs(source)

        return self.reached
