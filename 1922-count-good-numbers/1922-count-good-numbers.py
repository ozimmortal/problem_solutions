class Solution:
    def countGoodNumbers(self, n: int) -> int:
        even , prime = (n + 1) // 2 , n // 2
        mod = (10**9 + 7)
        return( pow(5, even, mod) * pow(4, prime, mod)) % mod 
        
