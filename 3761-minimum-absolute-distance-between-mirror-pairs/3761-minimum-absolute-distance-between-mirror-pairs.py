class Solution:
    def minMirrorPairDistance(self, nums: List[int]) -> int:
        
        def r(n):
            n = str(n)[::-1]
            return int(n)
        
        d = defaultdict(list)
        res = float('inf')
        for i , n in enumerate(nums):
            nr = r(n)
            if n in d:
                res = min(res , abs( i - d[n]))
            nr = r(n)
            d[nr] = i
           
                
           
        return res if res!=float('inf') else -1