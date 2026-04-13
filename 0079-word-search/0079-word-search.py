class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        
        def valid(r , c):
            return 0 <= r < len(board) and 0 <= c < len(board[0])

        def backtrack(seen, row ,col ,i):
            if  i == len(word):
                return True

            directions = [(0 , 1) , (1, 0) , (-1 , 0) , (0 , -1)]
            for dx ,dy in directions:
                nr , nc = row + dy , col + dx
                if valid(nr , nc) and (nr , nc) not in seen :
                    if board[nr][nc] == word[i]:
                        seen.add((nr ,nc))
                        if backtrack(seen , nr,nc ,i + 1):
                            return True
                        seen.remove((nr ,nc))
            return False
            
        for row in range(len(board)):
            for col in range(len(board[0])):
                if board[row][col] == word[0] and backtrack({(row , col)} , row , col , 1):
                    return True
        return False
        


                    

