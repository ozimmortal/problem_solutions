class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        
        def backtrack(curr , s):

            if sum(curr) == target:
                res.append(curr[:])
                return
            
            for i in range(s ,len(candidates)):
                t = sum(curr)
                n = candidates[i]
                if t + n  <= target:
                    curr.append(n)
                    backtrack(curr , i)
                    curr.pop()
        
        res = []
        backtrack([] , 0)
        return res