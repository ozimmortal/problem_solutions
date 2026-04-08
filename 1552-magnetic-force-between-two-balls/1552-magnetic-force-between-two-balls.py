class Solution:
    def maxDistance(self, position: List[int], m: int) -> int:
        position.sort()

        def check(x):
            n = len(position)
            b = 1
            last = position[0]
            for i in range(1 , n):
                if position[i] - last >= x:
                    last = position[i]
                    b += 1
                if b==m:
                    return True
            return False
        
        left = 1
        right = max(position) - min(position)
        while left <= right:
            mid = (left + right) // 2
            if check(mid):
                left = mid + 1
            else:
                right = mid - 1
      
        return left - 1



