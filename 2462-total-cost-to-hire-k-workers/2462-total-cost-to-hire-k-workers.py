class Solution:
    def totalCost(self, costs: List[int], k: int, candidates: int) -> int:
        
        n = len(costs)
        heap = []

        left = 0
        while left < candidates:
            print(costs[left] , "left")
            heapq.heappush(heap , (costs[left] , left))
            left += 1

        right = n - 1
        while right >  n - candidates - 1 and right >= candidates:
            print(costs[right] , "right")
            heapq.heappush(heap , (costs[right] , right))
            right -= 1
            
        total = 0
        while k:
            cost , idx = heapq.heappop(heap)
            total += cost
            print(cost , idx)
            if idx < left and left <= right:
                heapq.heappush(heap , (costs[left] , left))
                left += 1
            
            elif idx > right and right >= left:
                heapq.heappush(heap , (costs[right] , right))
                right -= 1
            k -= 1
        
        return total

                



        
        



