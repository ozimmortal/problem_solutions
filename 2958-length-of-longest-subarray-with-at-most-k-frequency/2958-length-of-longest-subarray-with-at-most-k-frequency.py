from collections import defaultdict
class Solution:
    def maxSubarrayLength(self, nums: List[int], k: int) -> int:
        
        co = defaultdict(int)
        l = ans = 0
        for r in range(len(nums)):
            co[nums[r]] += 1
            while co[nums[r]] > k:
                co[nums[l]] -= 1
                if co[nums[l]] == 0:
                    del co[nums[l]]
                l+=1
            ans = max(ans,(r-l+1))
        return ans 
