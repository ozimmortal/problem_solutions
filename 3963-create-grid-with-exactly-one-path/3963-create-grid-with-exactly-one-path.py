class Solution:
    def createGrid(self, m: int, n: int) -> list[str]:
        grid = [["#"]*n for _ in range(m)]
        start = (0 , 0)
        grid[0][0] = "."

        def valid(x , y):
            return 0 <= x < m and 0 <= y < n
        reached = False
        while not reached:

            rx , ry = start[0] , start[1] + 1
           
            if valid(rx , ry):
                start = (rx , ry)
                grid[rx][ry] = "."
                
            dx , dy = start[0] + 1 , start[1] 
            if valid(dx , dy):
                start = (dx , dy)
                grid[dx][dy] = "."
            if start[0] == m-1 and start[1] == n - 1:
                reached = True
        grid[m-1][n-1] = "."

        return ["".join(row) for row in grid]
        
        