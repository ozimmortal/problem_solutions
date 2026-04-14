class Solution:
    def numsSameConsecDiff(self, n: int, k: int) -> List[int]:
        
        def backtrack(path):

            if len(path) == n:
                if path[0] != '0':
                    res.append(int("".join(path)))
                return
            

            for i in range(10):
                if not path or abs(int(path[-1]) - i) == k:
                    path.append(str(i))
                    backtrack(path)
                    path.pop()
        
        res = []
        backtrack([])
        return res
            




