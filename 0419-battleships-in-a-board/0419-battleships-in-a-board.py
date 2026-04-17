class Solution:
    def countBattleships(self, board: List[List[str]]) -> int:

        def valid(r ,c):
            return 0 <= r < m and 0 <= c < n
        
        def dfs(node):
            directions = [ (0, 1) , (0 , -1), (1 , 0) , (-1, 0) ]
            
            r , c = node
            if  not valid(r ,c) or board[r][c] == ".":
                return

            for dx , dy in directions:
                x , y = r + dx , c + dy
                if valid(x ,y) and board[x][y] == "X":
                    if (x , y) not in seen:
                        seen.add((x ,y))
                        dfs((x ,y))                      
        
        seen = set()
        count = 0
        m , n = len(board) , len(board[0])

        for row in range(m):
            for col in range(n):

                if board[row][col] == "X" and (row , col) not in seen:
                    seen.add((row , col))
                    dfs((row ,col))
                    count += 1
        return count