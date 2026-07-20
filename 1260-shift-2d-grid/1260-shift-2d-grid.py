class Solution:
    def shiftGrid(self, grid: List[List[int]], k: int) -> List[List[int]]:
        
        m , n = len(grid), len(grid[0])
        t = m * n

        i = 0
        fl = [0] * (t)
        for r in range(m):
            for c in range(n):
                num = grid[r][c]
                sh = k % t
                sh_idx =  (i + sh) % t
                fl[sh_idx] = num
                i += 1

        return [fl[d: d+n] for d in range(0 , t , n) ]
        