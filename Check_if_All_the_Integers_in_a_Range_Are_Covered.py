class Solution:
    def isCovered(self, ranges: List[List[int]], left: int, right: int) -> bool:
        ranges.sort()
        for s , e in ranges:
            if s > left:
                return False
            if e >= left:
                left = e + 1
            if left > right:
                return True
        return left > right

        