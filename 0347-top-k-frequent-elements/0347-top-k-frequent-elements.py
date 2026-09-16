class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        heap = []
        freq = Counter(nums)

        for num , cnt in freq.items():
            heapq.heappush(heap, (cnt , num))

            while len(heap) > k:
                heapq.heappop(heap)
            
        return [num for _ , num in heap]
