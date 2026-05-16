class Solution:
    def numOfMinutes(self, n: int, headID: int, manager: List[int], informTime: List[int]) -> int:
        
        graph = defaultdict(list)
        for i , node in enumerate(manager):
            if node != -1:
                graph[node].append(i)
        
        queue = deque([(headID , 0)])
        totaltime = 0
        while queue:
            node , curr = queue.popleft()
            time = informTime[node] + curr
            totaltime = max(totaltime , time)
            for i in graph[node]:
                queue.append((i , time))
        return totaltime