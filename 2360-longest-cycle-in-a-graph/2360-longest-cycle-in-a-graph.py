class Solution:
    def longestCycle(self, edges: List[int]) -> int:

        n = len(edges)
        graph = {}
        indegree = [0] * n

        for i , x in enumerate(edges):
            if x != -1:
                graph[i] = x
                indegree[x] += 1
            
        queue = deque([i for i in range(n) if indegree[i] == 0])
        removed = [False] * n
        while queue:
            node = queue.popleft()
            removed[node] = True

            if node in graph:
                child = graph[node]
                indegree[child] -= 1
                if indegree[child] == 0:
                    queue.append(child)

        def dfs(node , s):
            if visited[node]:
                return s
                
            visited[node] = True
            child = graph[node]
            return dfs(child , s + 1)

        visited = [False] * n
        ans = -1
        for i in range(n):
            if not visited[i] and not removed[i]:
                ans = max(ans , dfs(i , 0))
        return ans 

                