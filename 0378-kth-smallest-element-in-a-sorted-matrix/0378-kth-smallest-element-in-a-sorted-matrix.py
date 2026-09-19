class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        
        n  = len(matrix)
        heap = [(matrix[r][0] , r , 0) for r in range(min(n , k))]
        heapq.heapify(heap)

        for _ in range(k - 1):
            x , r , c = heapq.heappop(heap)
            if c + 1 < n:
                heapq.heappush(heap , (matrix[r][c + 1] , r , c + 1))
        
        return heap[0][0]
            