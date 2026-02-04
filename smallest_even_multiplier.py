class Solution:
    def smallestEvenMultiple(self, n: int) -> int:
        while n < 300:
            if n%2 == 0 and n%n == 0:
                return n
            n *= 2
        
        