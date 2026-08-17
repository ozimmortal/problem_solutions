class Solution:
    def minimumSize(self, nums: List[int], maxOperations: int) -> int:
        
        def check(max_balls):
            ops = 0
            for n in nums:
                ops += ceil(n / max_balls) - 1
                if ops > maxOperations: return False
            return True
        
        left , right = 1 , max(nums)
        while left <= right:
            mid = (left + right) // 2
            if check(mid):
                right = mid - 1
            else:
                left = mid + 1
        
        return left