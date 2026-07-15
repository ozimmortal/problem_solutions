class Solution:
    def gcdOfOddEvenSums(self, n: int) -> int:
        return gcd(n, n + 1) * n
