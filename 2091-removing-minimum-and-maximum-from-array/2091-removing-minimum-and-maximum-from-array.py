class Solution:
    def minimumDeletions(self, nums: List[int]) -> int:
        
        n = len(nums)
        max_idx = nums.index(max(nums))
        min_idx = nums.index(min(nums))

        ans = float('inf')
        # remove from the front
        ans = min(ans , max(max_idx, min_idx) + 1)
        # remove from the back
        ans = min(ans , n - min(max_idx, min_idx))
        # remove from front for one remove on from back
        f , b =  min(max_idx, min_idx) + 1, n - max(max_idx, min_idx)
        ans = min(ans , f + b)

        return ans