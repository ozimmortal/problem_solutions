class Solution:
    def minSumOfLengths(self, arr: List[int], target: int) -> int:
        
        dp = [inf] * len(arr)
        res = inf
        l , curr = 0 , 0
        for r in range(len(arr)):
            curr += arr[r]

            while curr > target:
                curr -= arr[l]
                l += 1
            
            dp[r] = dp[r - 1] if r - 1 >= 0 else inf
            if curr == target:
                res = min(res , r - l + 1 + dp[l - 1] if l - 1 >= 0 else inf)
                dp[r] = min(dp[r], r - l + 1)
        
        return -1 if res == inf else res

