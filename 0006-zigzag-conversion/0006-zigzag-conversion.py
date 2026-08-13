class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows == 1: return s

        l = len(s)
        res = []
        for r in range(numRows):
            incr = (numRows - 1) * 2
            for i in range(r , l, incr):
                res.append(s[i])
                if 0 < r < numRows - 1 and i + incr - 2 * r < l:
                    res.append(s[i + incr - 2 * r])
        
        return "".join(res)
