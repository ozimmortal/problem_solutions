class Solution:
    def maximizeSweetness(self, sweetness: List[int], k: int) -> int:
        def check(x):
            c = 0
            d = 0
            for s in sweetness:
                c += s
                if c >= x:
                    d += 1
                    c =0
            return k + 1 <= d
        
        left = min(sweetness)
        right = sum(sweetness)
        
        while left <= right:
            mid = (left + right) // 2
            if check(mid):
                left = mid + 1
            else:
                right = mid - 1
        return left - 1         

