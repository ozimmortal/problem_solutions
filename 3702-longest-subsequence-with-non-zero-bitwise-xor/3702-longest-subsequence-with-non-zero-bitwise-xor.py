class Solution:
    def longestSubsequence(self, nums: List[int]) -> int:
        
        t = 0
        all_zero = True
        for n in nums:
            t ^= n
            if n > 0:
                all_zero = False
        
        if t > 0: return len(nums)
        return len(nums) - 1 if not all_zero else 0


