class Solution:
    def longestSubsequence(self, arr: List[int], difference: int) -> int:
        
        dp = defaultdict(int)
        ans = 0
        for n in arr:
            dp[n] = dp[n - difference] + 1
            ans = max(ans , dp[n])
        
        return ans