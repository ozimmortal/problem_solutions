class Solution:
    def findSubsequences(self, nums: List[int]) -> List[List[int]]:
        res = set()

        def backtrack(curr , i):

            if len(curr) >= 2:
                res.add(tuple(curr[:]))

            for j in range(i , len(nums)):
                if not curr or curr[-1] <= nums[j]:
                    curr.append(nums[j])
                    backtrack(curr , j + 1)
                    curr.pop()   


        backtrack([] , 0)
        return [list(a) for a in res]