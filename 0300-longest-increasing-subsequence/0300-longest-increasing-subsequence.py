class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        
        memo = {}
        def dp(start):
            if start in memo:
                return memo[start]

            best = 1
            for i in range(start + 1 , len(nums)):
                if nums[i] > nums[start]:
                    best = max(best, 1 + dp(i))
            
            memo[start] = best 
            return best
        
        res = 1
        for i in range(len(nums)):
            res = max(res , dp(i))
        return res