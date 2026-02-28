class Solution:
    def subarraysWithKDistinct(self, nums: List[int], k: int) -> int:
        
        c = defaultdict(int)
        lf,ln , res = 0 , 0 , 0

        for r in range(len(nums)):

            c[nums[r]] += 1

            while len(c) > k:
                c[nums[ln]] -= 1
                if c[nums[ln]] == 0:
                    del c[nums[ln]]
                ln += 1
                lf = ln
            while c[nums[ln]] > 1:
                c[nums[ln]] -= 1
                ln += 1

            if len(c) == k:
                res += ln -lf + 1
        return res        