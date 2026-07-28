class Solution:
    def totalHammingDistance(self, nums: List[int]) -> int:
        
        ans = 0
        for i in range(32):
            cnt = defaultdict(int)
            for num in nums:
                num >>= i
                cnt[num & 1] += 1
            ans += cnt[0] * cnt[1]
        
        return ans
