class Solution:
    def longestArithSeqLength(self, nums: List[int]) -> int:
        n = len(nums)
        dp = [defaultdict(int)  for _ in range(n)]
        ans = 0
        for i in range(n):
            for j in range(i):
                diff = nums[j] - nums[i]
                dp[i][diff] = max(dp[i][diff] , dp[j][diff] + 1 if dp[j][diff] else 2)
                ans = max(dp[i][diff] , ans)
        return ans

        
