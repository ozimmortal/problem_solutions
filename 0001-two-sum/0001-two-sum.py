class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        cnt = Counter()
        for i in range(len(nums)):
            t = target - nums[i]
            if t in cnt:
                return [cnt[t], i]
            
            cnt[nums[i]] = i


        