class Solution:
    def maxScore(self, nums1: List[int], nums2: List[int], k: int) -> int:
        
        pairs = [(n1 ,n2) for n1 ,n2 in zip(nums1 , nums2)]
        pairs.sort(key = lambda x : x[1], reverse=True)

        heap = []
        res , total = 0 , 0

        for n1 , n2 in pairs:
            total += n1
            heapq.heappush(heap , n1)

            if len(heap) > k:
                x = heapq.heappop(heap)
                total -= x
            
            if len(heap) == k:
                res = max(res , total * n2)
        
        return res

        