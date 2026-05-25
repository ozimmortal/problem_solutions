class Solution:
    def eventualSafeNodes(self, graph: List[List[int]]) -> List[int]:
        
        g = defaultdict(list)
        indegree = [len(graph[i]) for  i in range(len(graph))]
        for i in range(len(graph)):
            for n in graph[i]:
                g[n].append(i)
        
        
        queue = deque([i for i in range(len(graph)) if indegree[i] == 0])
        order = []

        while queue:
            node = queue.popleft()
            order.append(node)

            for dep in g[node]:
                indegree[dep] -= 1
                if indegree[dep] == 0:
                    queue.append(dep)
        
        return sorted(order)


