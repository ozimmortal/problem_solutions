class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        cnt = Counter(nums)
        n = len(nums)

        for k, val in cnt.items():
            if val > n// 2:
                return k