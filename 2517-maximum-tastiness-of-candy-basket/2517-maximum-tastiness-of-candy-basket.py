class Solution:
    def maximumTastiness(self, price: List[int], k: int) -> int:
        
        price.sort()
        def check(x):
            t = 1
            l = price[0]
            for i in range(1 , len(price)):
                if abs(price[i] - l) >= x:
                    t += 1
                    l = price[i]
            return t >= k

        left , right = 0 , price[-1]
        while left <= right:
            mid = (left + right) // 2
            if check(mid):
                left = mid + 1
            else:
                right = mid - 1
        return right
