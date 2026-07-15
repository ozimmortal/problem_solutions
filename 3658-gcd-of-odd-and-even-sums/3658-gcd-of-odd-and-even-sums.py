class Solution:
    def gcdOfOddEvenSums(self, n: int) -> int:
        sumOdd , sumEven = 0 , 0
        for i in range(1 , (n * 2 + 1)):
            if i % 2 == 0:
                sumEven += i
                continue
            sumOdd += i
        return gcd(sumOdd, sumEven)
