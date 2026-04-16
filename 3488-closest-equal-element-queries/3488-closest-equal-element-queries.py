class Solution:
    def solveQueries(self, nums: List[int], queries: List[int]) -> List[int]:
        
        c = defaultdict(list)
        for i , n in enumerate(nums):
            c[n].append(i)
        
        res = [-1] * len(queries)
        lg = len(nums) 
        for i , q in enumerate(queries):
            n = nums[q]
            arr = c[n]
            idx = bisect_left(arr , q)
            
            l = len(arr)
            if l > 1:
                to_left =(lg  - arr[-1]) + arr[idx]   if idx == 0 else abs(arr[idx] - arr[idx - 1])
                to_right = (lg  - arr[idx]) + arr[0]  if idx == l -1 else abs(arr[idx] - arr[idx + 1])
                res[i]  = min(to_left , to_right)
                
        return res