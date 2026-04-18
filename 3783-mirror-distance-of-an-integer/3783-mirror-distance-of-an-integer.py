class Solution:
    def mirrorDistance(self, n: int) -> int:
        
        def rev(x):
            return int(str(x)[::-1])
        return abs(n - rev(n))