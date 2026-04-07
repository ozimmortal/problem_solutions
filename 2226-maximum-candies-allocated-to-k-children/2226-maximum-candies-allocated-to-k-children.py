class Solution:
    def maximumCandies(self, candies: List[int], k: int) -> int:
        
        
        
        def check(c):
            s = 0

            for i in candies:
                s += i // c
            return s >= k

        left =  1
        right = max(candies)

        while left <= right:
            c = (left + right) // 2
            print(left , right , c)
            if check(c):
                left = c + 1
            else:
                right = c - 1
        
        return left - 1
        