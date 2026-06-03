class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        if len(stones) == 1:
            return stones[0]

        heap = []
        for stone in stones:
            heapq.heappush(heap , -stone)
        
        while len(heap) > 1:
            x ,  y = heapq.heappop(heap) , heapq.heappop(heap)
            left = abs(abs(x) - abs(y))
            if left > 0:
                heapq.heappush(heap , -left)
        return abs(heap[0]) if len(heap) > 0 else 0
