class Solution:
    def makeIntegerBeautiful(self, n: int, target: int) -> int:
        def sum(x):
            t = 0
            while x > 0:
                t += x % 10
                x = x//10
            return t

        ans , div = 0 , 10
        while sum(n) > target:
            m = n % div
            ans += div - m
            n += div - m
            div *= 10
        return ans  

            

