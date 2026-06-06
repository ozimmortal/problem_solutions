class Solution:
    def minStoneSum(self, piles: List[int], k: int) -> int:
        
        total = sum(piles)
        heap = []
        for pile in piles:
            heapq.heappush(heap , -pile)

        for _ in range(k):
            pile = -heapq.heappop(heap) 
            removed = pile // 2
            total -= removed
            heapq.heappush(heap, -(pile - removed))
        return total
