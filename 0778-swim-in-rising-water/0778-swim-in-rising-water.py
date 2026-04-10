class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        n , m = len(grid) , len(grid)
        def inside(x , y):
            return 0<= x < n and 0 <= y < m

        def check(l):
            seen = {(0 ,0)}
            def dfs(x ,y):
                directions = [(0,1) , (1, 0) , (-1 ,0) , (0 , -1)]

                if x == len(grid) - 1 and y == len(grid) - 1:
                    return True
                
                if inside(x , y):
                    for dx , dy in directions:
                        nx , ny = x +dx , y + dy
                        if inside(nx ,ny) and grid[nx][ny] <= l and (nx , ny) not in seen:
                            seen.add((nx ,ny)) 
                            if dfs(nx , ny):
                                return True
                return False
            return dfs(0 , 0)
            
        l ,r = grid[0][0] , n*n -1
        while l <= r:
            mid = (l + r)// 2
            if check(mid):
                r = mid -1
            else:
                l = mid + 1
        return l