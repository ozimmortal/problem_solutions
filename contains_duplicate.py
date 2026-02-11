from collections import Counter
class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        return max(Counter(nums).values()) != 1