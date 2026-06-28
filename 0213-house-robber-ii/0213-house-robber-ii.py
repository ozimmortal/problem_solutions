class Solution:
    def rob(self, nums: List[int]) -> int:
        
        if len(nums) == 1: return nums[0]
        
        @cache
        def dp(i , limit):
            if i >= limit: return 0
            return max(dp(i + 2, limit) + nums[i] , dp(i + 1 , limit))

        n = len(nums)
        return max(dp(0 , n -1) , dp(1 , n))
