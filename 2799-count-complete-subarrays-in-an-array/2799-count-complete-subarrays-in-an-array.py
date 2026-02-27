class Solution:
    def countCompleteSubarrays(self, nums: List[int]) -> int:
        k = len(set(nums))
        res = 0
        left = 0
        c = defaultdict(int)
        for right in range(len(nums)):
            c[nums[right]] += 1

            while len(c) == k:
                res += len(nums) - right
                c[nums[left]] -= 1
                if c[nums[left]] == 0:
                    del c[nums[left]]
                left += 1
        return res

