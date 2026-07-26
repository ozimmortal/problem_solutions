class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        nums.sort(key = lambda x : abs(x), reverse=True)
        p1 , p2 = abs(nums[0]) , abs(nums[1])
        return p1 * p2 * (10 ** 5)