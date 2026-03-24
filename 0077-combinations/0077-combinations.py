class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        res = []
        def solve(s , comb):

            if  len(comb) == k:
                res.append(comb[:])
                return
            for i in range(s,n+1):
                comb.append(i)
                solve(i+1,comb)
                comb.pop()
        solve(1,[])
        return res



            

            

            