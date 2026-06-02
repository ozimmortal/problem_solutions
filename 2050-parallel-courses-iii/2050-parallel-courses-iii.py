class Solution:
    def minimumTime(self, n: int, relations: List[List[int]], time: List[int]) -> int:
        
        graph = defaultdict(list)
        indegree = [0] * (n + 1)
        
        for x , y in relations:
            graph[x].append(y)
            indegree[y] += 1
        
        endTime = [0] * (n + 1)
        queue = deque()

        for i in range(1 , n+1):
            if indegree[i] == 0:
                queue.append(i)
                endTime[i] = time[i - 1]

        while queue:
            node = queue.popleft()
            
            for n in graph[node]:
                endTime[n] = max(endTime[n] , endTime[node] + time[n - 1])
                indegree[n] -= 1
                if indegree[n] == 0:
                    queue.append(n)
        
        return max(endTime)