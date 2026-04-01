class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        
        def check(cap):
            currCap = cap
            ships = 1

            for w in weights:
                if currCap - w < 0:
                    ships += 1
                    currCap = cap
                currCap -= w
            return ships <= days
        
        left = max(weights)
        right = sum(weights)

        res = right

        while left <= right:
            cap = (left + right) // 2

            if check(cap):
                res = min(res,cap)
                right = cap - 1
            else:
                left = cap + 1
        return res
                