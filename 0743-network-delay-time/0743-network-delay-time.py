class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        
        graph = defaultdict(list)
        for u , v ,w in times:
            graph[u-1].append((v - 1 , w))
        
        k = k - 1
        delay = [float('inf')] * n
        delay[k] = 0

        heap = []
        heapq.heappush(heap, (k, 0))

        while heap:
            node , time = heapq.heappop(heap)
            if time > delay[node]:
                continue
            
            for nei , curr_t in graph[node]:
                new_t = time + curr_t

                if new_t < delay[nei]:
                    heapq.heappush(heap , (nei , new_t))
                    delay[nei] = new_t
        final_time = max(delay)        
        return -1 if final_time == float('inf') else final_time
