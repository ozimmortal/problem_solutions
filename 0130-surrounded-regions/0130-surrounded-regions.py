class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """

        def valid(x ,y):
            return 1 <= x < m and 1 <= y < n and board[x][y]=="O"
    
        def dfs(node):
            x ,y = node

            for dx , dy in directions:
                nx , ny = x + dx , y + dy

                if valid(nx , ny) and (nx ,ny) not in seen:
                    seen.add((nx ,ny))
                    dfs((nx , ny))
        
        
        directions= [(1 , 0) , (0 , 1) , (-1 , 0), (0 ,-1)]
        m , n = len(board) , len(board[0])
        seen = set()

        for i in [0 , m - 1]:
            for j in range(n):
                if board[i][j] == "O" and (i , j) not in seen:
                    seen.add((i , j))
                    dfs((i , j))
        for j in [0 , n - 1]:
            for  i in range(m):
                if board[i][j] == "O" and (i , j) not in seen:
                    seen.add((i , j))
                    dfs((i , j))
        
        for r in range(m):
            for c in range(n):
                if board[r][c] == "O" and (r , c) not in seen:
                    board[r][c] = "X"

        return board
                

        