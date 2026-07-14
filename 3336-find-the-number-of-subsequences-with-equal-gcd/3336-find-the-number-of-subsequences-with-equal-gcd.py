class Solution:
    def subsequencePairCount(self, nums: List[int]) -> int:
        n = len(nums)
        MOD = 10 ** 9 + 7
        @cache
        def dp(i , gcd1 , gcd2):

            if i == len(nums):
                return 1 if gcd1 == gcd2 else 0
            
            return dp(i + 1,gcd1,gcd2) % MOD + dp(i + 1, gcd(gcd1 , nums[i]),gcd2) % MOD + dp(i + 1,gcd1, gcd(gcd2, nums[i])) % MOD
        
        return (dp(0 , 0 , 0) - 1) % MOD