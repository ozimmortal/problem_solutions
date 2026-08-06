class Solution:
    def smallestNumber(self, n: int, t: int) -> int:
        
        def mul_dig(n):
            ans = 1
            while n > 0:
                ans *= n % 10
                n //= 10
            return ans

        for nu in range(n , n + 10):
            if mul_dig(nu) % t == 0:
                return nu