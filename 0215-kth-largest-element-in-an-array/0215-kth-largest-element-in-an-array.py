class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        
        heap =  [-n for n in nums]
        heapq.heapify(heap)
        while k - 1 > 0:
            print( heapq.heappop(heap))
            k -= 1
        return heap[0] * -1