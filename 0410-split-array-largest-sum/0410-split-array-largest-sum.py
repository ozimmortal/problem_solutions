class Solution:
    def splitArray(self, nums: List[int], k: int) -> int:
        
        def check(s):
            sub = 1
            t = 0

            for n in nums:
                t += n
                if t > s:
                    sub+= 1
                    t = n
            return sub <= k
        
        left = max(nums)
        right = sum(nums)

        while left <= right:
            mid = left + ((right - left) // 2)
            if check(mid):
                right = mid -1
            else:
                left = mid + 1
        return left 