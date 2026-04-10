class Solution:
    def latestDayToCross(self, row: int, col: int, cells: List[List[int]]) -> int:
        
        def inside(x , y):
            return 0<= x < row and 0 <= y < col

        def check(l):
            board = [[0] * col for _ in range(row)]
            for x,y in cells[:l]:
                board[x -1][y - 1] = 1
            q = deque()
        
            for j in range(col):
                if board[0][j] == 0:
                    q.append((0 , j))
                    board[0][j] = 1
            while q:

                x , y = q.popleft()

                if x == row - 1:
                    return True
                
                directions = [(0,1), (-1,0), (0,-1), (1,0)]
                for dx , dy in directions:
                    nx , ny = x + dx , y + dy
                    if inside(nx,ny) and board[nx][ny] == 0:
                        q.append((nx,ny))
                        board[nx][ny] = 1

            return False

        l ,r = 0 , row * col
        while l <=r:
            mid = (l + r)//2
            if check(mid):
                l = mid + 1
            else:
                r = mid - 1
        return l - 1
            
                       
            
           