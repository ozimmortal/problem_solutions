class Solution:
    def connectSticks(self, sticks: List[int]) -> int:
        
        if len(sticks) == 1:
            return 0

        heapq.heapify(sticks)
        cost = 0
        while len(sticks) > 1:
            a , b = heapq.heappop(sticks) , heapq.heappop(sticks)
            cost += a + b
            heapq.heappush(sticks , a + b)
        
        return cost 

