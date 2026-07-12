class Solution:
    def arrayRankTransform(self, arr: List[int]) -> List[int]:
        n = len(arr)
        if len(arr) == 0: return []

        nums = [[val , i]  for i , val in enumerate(arr)]

        nums.sort()
        res = [1] * n
        res[nums[0][1]] = 1
        for i in range(1 , n):
            bval , bidx = nums[i - 1]
            cval , cidx = nums[i]
            
            res[cidx] = res[bidx] if cval == bval else res[bidx] + 1
        
        return res