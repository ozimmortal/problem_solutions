class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:

        n = len(weights)
        def check(size):
            total = 0
            w = 0
            while w < n:
                curr = 0
                while w < n and curr + weights[w] <= size:
                    curr += weights[w]
                    w += 1
                total += 1
            return total <= days

        left , right = max(weights) , sum(weights)      
        while left <= right:
            mid = (left + right) // 2
            if check(mid):
                right = mid - 1
            else:
                left = mid + 1
        
        return left