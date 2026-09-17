class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        
        cnt, curr = defaultdict(int), 0
        cnt[0] = 1
        res = 0

        for num in nums:
            curr += num
            res += cnt[curr % k]
            cnt[curr % k] += 1
        
        return res