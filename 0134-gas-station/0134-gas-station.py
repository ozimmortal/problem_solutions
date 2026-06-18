class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        
        n = len(gas)
        if sum(gas) < sum(cost):
            return  -1

        
        total = 0
        ans = 0
        for i in range(n):
            dif = gas[i] - cost[i]
            total += dif

            if total < 0:
                total = 0
                ans = i + 1
        return ans

        