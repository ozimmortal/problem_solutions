class Solution:
    def reachableNodes(self, n: int, edges: List[List[int]], restricted: List[int]) -> int:
        
        graph = defaultdict(list)
        for x ,y in edges:
            graph[x].append(y)
            graph[y].append(x)

        restricted = set(restricted)
        def dfs(node):
            for n in graph[node]:
                if n not in restricted and n not in seen:
                    self.visited += 1
                    seen.add(n)
                    dfs(n)

        self.visited = 0
        seen = {0}
        if 0 not in restricted:
            self.visited += 1
            dfs(0)

        return self.visited
