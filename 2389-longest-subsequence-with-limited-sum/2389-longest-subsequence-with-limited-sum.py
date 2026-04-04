class Solution:
    def answerQueries(self, nums: List[int], queries: List[int]) -> List[int]:
        res = []
        nums.sort()
        prefix = [nums[0]]

        for i in range(1,len(nums)):
            prefix.append(prefix[i - 1] + nums[i])

        for q in queries:
            i = bisect_right(prefix,q)
            res.append(i)
        return res