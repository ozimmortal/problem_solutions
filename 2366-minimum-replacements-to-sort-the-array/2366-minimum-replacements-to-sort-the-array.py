class Solution:
    def minimumReplacement(self, nums: List[int]) -> int:
        s = 0
        r = nums[-1]

        for i in range(len(nums)-2 , -1 , -1):
            l = nums[i]

            if l > r:
                p = math.ceil(l / r)
                s += p -1
                r = l // p
            else:
                r = l

        return s

            

        