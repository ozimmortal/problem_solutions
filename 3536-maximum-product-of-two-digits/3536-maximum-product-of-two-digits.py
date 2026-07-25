class Solution:
    def maxProduct(self, n: int) -> int:
        
        digits = []
        while n > 0:
            d = n % 10
            digits.append(d)
            n //= 10
        
        n = len(digits)
        pd = []
        for i in range(n):
            for j in range(i + 1 , n):
                pd.append(digits[i] * digits[j])
        
        return max(pd)
        
