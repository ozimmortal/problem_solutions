class Solution:
    def gcdValues(self, nums: List[int], queries: List[int]) -> List[int]:
        
        m = max(nums)
        cnt = [0] * (m + 1)
        for n in nums:
            cnt[n] += 1
        
        gcd = [0] * (m + 1)
        for i in range(m, 0 , -1):
            k = sum(cnt[i::i])
            gcd[i] = (k * (k - 1)) // 2  - sum(gcd[i * 2::i])
        
        for i in range(1 , m + 1):
            gcd[i] += gcd[i - 1]
        
        return [bisect_left(gcd , q + 1) for q in queries]
    