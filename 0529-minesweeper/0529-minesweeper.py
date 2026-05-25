class Solution:
    def updateBoard(self, board: List[List[str]], click: List[int]) -> List[List[str]]:
        m , n= len(board) , len(board[0])
        directions = [(1 , 0) , (0 , 1), (-1 , 0) , (0 , -1), (1 , 1), (-1 , -1), (-1 ,1), (1 , -1)]

        def valid(x ,y):
            return 0 <= x < m and 0 <= y < n
        
        def check(x , y):
            count = 0
            for dx ,dy in directions:
                nx , ny = x +dx , y + dy
                if valid(nx ,ny) and board[nx][ny] == "M":
                    count += 1
            return count
        
        x , y = click
        def dfs(x, y):
            if board[x][y] != "E":
                return
                
            count = check(x , y)
            if count > 0:
                board[x][y] = str(count)
                return
            else:
                 board[x][y] = "B"

            for dx ,dy in directions:
                nx , ny = x +dx , y + dy
                if valid(nx ,ny) and  board[nx][ny] == "E":
                    dfs(nx ,ny)
        if board[x][y] == "M":
            board[x][y] = "X"
            return board

        dfs(x , y)
        return board


