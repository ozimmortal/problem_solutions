class Solution:
    def reverseSubmatrix(self, grid: List[List[int]], x: int, y: int, k: int) -> List[List[int]]:
        m , n = len(grid) , len(grid[0])
        last = x + k - 1
        for i in range(x , x + (k)// 2 ):
            for j in range(y , y + k):
                grid[i][j] , grid[last][j] = grid[last][j] , grid[i][j]
            last -= 1
        
        return grid

            
        

        