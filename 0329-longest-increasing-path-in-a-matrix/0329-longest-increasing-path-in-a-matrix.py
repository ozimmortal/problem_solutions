class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        
        def valid(r , c):
            return 0 <= r < m and 0 <= c < n

        @cache
        def dfs(x ,y):
            
            dis = 1
            num = matrix[x][y]
            for dx , dy in directions:
                nx , ny = x + dx , y + dy
                if valid(nx , ny) and matrix[nx][ny] > num:
                    dis = max(dis, 1 + dfs(nx, ny))

            return dis
        res = 1
        m , n = len(matrix) , len(matrix[0])
        directions = [(1 , 0) , (0 , 1) , (-1 , 0), (0 , -1)]
        for r in range(m):
            for c in range(n):
                res = max(res , dfs(r ,c))
        return res


            
            
