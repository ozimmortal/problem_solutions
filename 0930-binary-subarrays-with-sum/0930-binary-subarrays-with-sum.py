from collections import defaultdict 

class Solution:
    def numSubarraysWithSum(self, nums: List[int], goal: int) -> int:
        co = defaultdict(int)
        co[0] = 1
        curr = ans = 0

        for n in nums:
            curr += n
            ans += co[curr - goal]
            co[curr] += 1
        return ans
    