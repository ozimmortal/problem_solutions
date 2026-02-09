from collections import defaultdict
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        c = defaultdict(int)
        
        for i in range(len(nums)):
            r = target - nums[i]
            if r in c :
                return [c[r],i ]
            else:
                c[nums[i]] = i


