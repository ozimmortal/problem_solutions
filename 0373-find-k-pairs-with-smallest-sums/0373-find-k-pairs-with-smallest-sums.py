class Solution:
    def kSmallestPairs(self, nums1: List[int], nums2: List[int], k: int) -> List[List[int]]:

        m , n = len(nums1) , len(nums2)
        heap = [(nums1[0] + nums2[0] , 0 , 0)]
        seen = {(0 , 0)}

        res = []
        while k and heap:
            _, p1 , p2 = heapq.heappop(heap)
            res.append([nums1[p1] , nums2[p2]])

            if p1 + 1 < m and (p1 + 1 , p2) not in seen:
                heapq.heappush(heap , (nums1[p1 + 1] + nums2[p2] , p1 + 1 , p2))
                seen.add((p1 + 1 , p2))

            if p2 + 1 < n  and  (p1 , p2 + 1) not in seen:
                heapq.heappush(heap , (nums1[p1] + nums2[p2 + 1], p1 , p2 + 1))
                seen.add((p1, p2 + 1))

            k -= 1
        
        return res

        

        
