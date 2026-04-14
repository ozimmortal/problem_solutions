class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()

        def backtrack(path , i , s):

            if s == target:
                res.append(path[:])
                return
            
            for j in range(i , len(candidates)):
                n = candidates[j]
                
                if j > i and n == candidates[j - 1]:
                    continue
                if s + n > target:
                    break

                path.append(n)
                backtrack(path , j + 1 , s + n)
                path.pop()
            
        res = []
        backtrack([] , 0 , 0)
        return res