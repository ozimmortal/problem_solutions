class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        counts = Counter(nums)
        heap = []
        for key , freq  in counts.items():
            heapq.heappush(heap , (freq , key))

            if len(heap) > k:
                heapq.heappop(heap)
        
        return [pair[1] for pair in heap]
