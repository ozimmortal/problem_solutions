class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:

        def backtrack(path , s):

            if len(path) == k and s == n:
                t = tuple(sorted(path))
                if t not in res:
                    res.add(t) 
                return
            
            for i in range(1,10):
                if i not in path:
                    path.add(i)
                    s += i
                    backtrack(path , s)
                    path.remove(i)
                    s -= i
        
        res = set()
        backtrack(set() , 0)
        return [list(a) for a in res]



        