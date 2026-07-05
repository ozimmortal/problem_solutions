class Solution:
    def gameOfLife(self, board: List[List[int]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        def valid(r ,c):
            return 0 <= r < m and 0 <=c < n
        
        def dead_or_alive(r ,c , cnt):
            cell = copy_board[r][c]
            if cell == 0:
                return 1 if cnt == 3 else 0

            return 1 if cnt == 2 or cnt == 3 else 0


        m , n = len(board) , len(board[0])
        copy_board = [board[i].copy() for i in range(m)]
        neighbours = [(0,1), (1,0), (-1,0), (0,-1),(-1, 1), (1 , -1) , (1,1) , (-1 , -1)]

        for r in range(m):
            for c in range(n):
                ncount = 0
                for dr ,dc in neighbours:
                    nr , nc = r + dr, c + dc
                    if valid(nr , nc):
                        ncount += copy_board[nr][nc]
                board[r][c] = dead_or_alive(r , c , ncount)
        

