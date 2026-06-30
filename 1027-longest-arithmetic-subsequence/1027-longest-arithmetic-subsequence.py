class Solution:
    def longestArithSeqLength(self, nums: List[int]) -> int:
        
        
        res = 0
        k = max(nums) - min(nums) + 1
        for  i in range(-k + 1 , k ):
            difference = i
            dp = defaultdict(int)
            ans = 0
            for n in nums:
                dp[n] = dp[n - difference] + 1
                ans = max(ans , dp[n])
            res = max(res , ans)
        
        return res

