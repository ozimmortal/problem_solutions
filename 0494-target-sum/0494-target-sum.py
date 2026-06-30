class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        
        @cache
        def dp(i , s):
            if i == n:
                return 1 if s == target else 0
            
            res = 0
            res +=  dp(i + 1 , s + nums[i]) + dp(i + 1 , s - nums[i])
            return res
            

        n = len(nums)
        return dp(0 , 0)
        

