class Solution:
    def twoCitySchedCost(self, costs: List[List[int]]) -> int:
        b = sorted(costs, key= lambda x : x[1] - x[0])
        n = len(costs)
        res = 0

        for i in range(0 , n//2):
            res += b[i][1]
        for i in range(n//2,n):
            res += b[i][0]
        print(b)
        return res
        