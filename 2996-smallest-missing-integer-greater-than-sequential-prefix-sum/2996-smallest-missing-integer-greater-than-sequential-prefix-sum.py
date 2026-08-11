class Solution:
    def missingInteger(self, nums: List[int]) -> int:
        arr = set(nums)
        pref = nums[0]
        for a, b in pairwise(nums):
            if a+ 1 != b:
                break
            pref += b

        while pref in arr:
            pref +=1
        return pref
                





            