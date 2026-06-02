class Solution:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        
        graph = defaultdict(list)
        indegree = [0] * n
        for x ,y in edges:
            graph[x].append(y)
            graph[y].append(x)
            indegree[x] += 1
            indegree[y] += 1
        
        queue = deque([[i , 0] for i in range(n) if indegree[i] == 1])
        seen = set([i for i in range(n) if indegree[i] == 1])
        order = defaultdict(list)
        last = 0
        while queue:
            node ,level = queue.popleft()
            order[level].append(node)

            for nxt in graph[node]:
                if nxt not in seen:
                    indegree[nxt] -= 1
                    if indegree[nxt] == 1:
                        queue.append([nxt , level + 1])
                        seen.add(nxt)
                        last  = level + 1
            
        return order[last] if last in order else [0]
        

            