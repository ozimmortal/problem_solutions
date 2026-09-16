class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        return any(val > 1 for _ , val in Counter(nums).items())
        