class Solution:
    def partitionArray(self, nums: List[int], k: int) -> int:
        
        nums.sort()
        x = 0
        ans = 1
        for i in range(1,len(nums)):
            d = nums[i] - nums[x]
            if d > k:
                x = i
                ans += 1
        return ans
