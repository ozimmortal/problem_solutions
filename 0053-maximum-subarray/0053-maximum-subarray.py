class Solution:
    def maxSubArray(self, nums: List[int]) -> int:

        @cache
        def dp(i):
            if i == len(nums) - 1:
                return nums[i]
            return max(nums[i] , nums[i] + dp(i + 1))
        
        return max(dp(i) for i in range(len(nums)))


       
        