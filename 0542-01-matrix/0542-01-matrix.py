class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        
        def valid(x , y):
            return 0 <= x < m and 0 <= y < n and mat[x][y] == 1
        
        queue = deque()
        seen = set()
        m , n = len(mat) , len(mat[0])

        for row in range(m):
            for col in range(n):
                if mat[row][col] == 0:
                    queue.append((row ,col , 1))
                    seen.add((row, col))

        directions = [(1,0),(0 , 1) , (-1, 0 ),(0 , -1)]
        while queue:

            x , y , s = queue.popleft()
            for dx , dy in directions:
                nx , ny = x + dx , y + dy
                if valid(nx , ny) and (nx , ny) not in seen:
                    queue.append((nx , ny , s + 1))
                    seen.add((nx , ny))
                    mat[nx][ny] = s
        
        return mat
