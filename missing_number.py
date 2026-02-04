class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        se = set(nums)
        for i in range(len(nums) + 1):
            if i not in  se:
                return i
        return 