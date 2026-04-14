class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        co = Counter(nums)

        def backtrack(path):

            if len(path) == len(nums):
                res.append(path[:])
                return
          
            
            for n in co:
                if co[n] > 0:
                    path.append(n)
                    co[n] -= 1
                    backtrack(path)
                    path.pop()
                    co[n] += 1

        res = []
        backtrack([])
        return res                