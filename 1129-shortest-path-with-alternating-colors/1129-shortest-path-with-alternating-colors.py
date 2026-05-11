class Solution:
    def shortestAlternatingPaths(self, n: int, redEdges: List[List[int]], blueEdges: List[List[int]]) -> List[int]:
        graph = defaultdict(lambda: defaultdict(list))
        BC , RC = 1 , 0

        for x , y in redEdges:
            graph[RC][x].append(y)
        for x , y in blueEdges:
            graph[BC][x].append(y)

        res = [float('inf')] * n
        queue = deque([(0 , RC , 0), (0 , BC, 0)])
        seen = {(0,RC) , (0 , BC)}
        while queue:
            node , c , s = queue.popleft()
            res[node] = min(res[node] , s)

            for n in graph[c][node]:
                if (n , 1 - c) not in seen:
                    seen.add((n , 1 - c))
                    queue.append((n , 1 - c , s + 1))
                
        return [ -1 if i == float('inf') else i  for i in res ]


        