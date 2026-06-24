class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        
        if len(cost) == 1:
            return cost[0]

        b , t = cost[0] , cost[1]
        for curr in range(2 , len(cost)):
            b , t = t , min(b ,t) + cost[curr]
        
        return min(b ,t)