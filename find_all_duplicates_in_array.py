from collections import Counter
class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        c = Counter(nums)
        return [k for k , n in c.items() if n == 2 ]

        