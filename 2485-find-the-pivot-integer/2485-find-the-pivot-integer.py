class Solution:
    def pivotInteger(self, n: int) -> int:

        total = (n * (n + 1)) / 2
        for x in range(1 , n + 1):
            tx = (x * (x - 1)) / 2
            ty = total - tx - x

            if tx == ty: return x

        return -1
        