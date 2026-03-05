class Solution:
    def maxSumRangeQuery(self, nums: List[int], requests: List[List[int]]) -> int:
        
        dif = [0] * (len(nums) + 1)

        for l , r in requests:
            dif[l] += 1
            dif[r + 1] -= 1

        prefix = [dif[0]]

        for i in range(1, len(nums)):
            prefix.append(prefix[i - 1] + dif[i])

        ans = 0
        prefix.sort()
        nums.sort()
        for i in range(len(nums)):
            ans += prefix[i] * nums[i]

        return ans % (10 ** 9 + 7) 