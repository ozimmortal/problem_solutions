class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        
        
        curr, cnt = 0 , defaultdict(int)
        cnt[0] = 1
        res = 0

        for i in range(len(nums)):
            curr += nums[i]
            res += cnt[curr - k]
            cnt[curr] += 1
        
        return res

