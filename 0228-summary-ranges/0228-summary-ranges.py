class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:

        if len(nums) == 0:
            return []
        res = []
        start , before = nums[0] , nums[0]
        for i in range(1 , len(nums)):
            dif = nums[i] - before
            if dif != 1:
                res.append(f"{start}->{before}" if start != before else f"{start}")
                start = nums[i]
            before = nums[i]
        
        res.append(f"{start}->{before}" if start != before else f"{start}")
        return res
        