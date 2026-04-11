class Solution:
    def minimumDistance(self, nums: List[int]) -> int:
        
        c = defaultdict(list)

        for i , n in enumerate(nums):
            c[n].append(i)
        
        res = float('inf')
        for k , v in c.items():
            leng = len(v)
            
            if leng >= 3:
                for i in range(leng-2):
                    f = 2 * (v[i+2] - v[i])
                    res = min(res , f)

        return res if res != float('inf') else -1