class Solution:
    def kthFactor(self, n: int, k: int) -> int:
        
        sf, bf = [] , []
        i = 1
        while i * i <= n:
            if n % i == 0:
                sf.append(i)
                if i != n // i:
                    bf.append(n // i)
            i += 1
        factors = sf + bf[::-1]
        return factors[k - 1] if k <= len(factors) else - 1

