class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        
        graph = defaultdict(list)
        for u , v ,w in flights:
            graph[u].append((v , w))
        
        stops = [float('inf')] * n

        heap = []
        heapq.heappush(heap, (0, src , 0))

        ans = float('inf')
        while heap:
            cost , node , s = heapq.heappop(heap)

            if node == dst:
                ans = min(ans , cost)
            
            if s > stops[node] or s > k:
                continue

            stops[node] = s
            for nei , curr_cost in graph[node]:
                heapq.heappush(heap , (curr_cost + cost, nei , s + 1))
                
        
        return -1 if ans == float('inf') else ans


            
        

        