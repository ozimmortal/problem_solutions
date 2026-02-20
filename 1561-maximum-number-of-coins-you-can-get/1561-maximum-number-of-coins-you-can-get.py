class Solution:
    def maxCoins(self, piles: List[int]) -> int:
        piles.sort(reverse=True)
        maxi = 0
        a, b, c = 0, 1, len(piles) - 1

        while b < c:
            maxi += piles[b]
            a += 2
            b += 2
            c -= 1


        return maxi
