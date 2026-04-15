class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        c = defaultdict(int)
        s = sorted(nums)

        for i,n in enumerate(s):
           if not n in c.keys():
                c[n] = i
        for i,n in enumerate(nums):
            nums[i] = c[n]
        return nums

        