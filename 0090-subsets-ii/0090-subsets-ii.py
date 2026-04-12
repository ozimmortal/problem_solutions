class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        res = []

        def backtrack(curr , i):
            if i > len(nums):
                return
            s = sorted(curr[:])
            if s not in res:
                res.append(s)
            for j in range(i , len(nums)):
                curr.append(nums[j])
                backtrack(curr , j + 1)
                curr.pop()

        backtrack([] , 0)
        return res