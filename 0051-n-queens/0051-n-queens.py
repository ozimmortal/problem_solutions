class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:

        def build(cols):
            board = []
            for col in cols:
                b = ["."]* n
                b[col]  = "Q"
                board.append("".join(b))
            return board

        def backtrack(row ,LD , RD , cols):

            if row == n:
                board = build(cols)
                res.append(board)
                return
            
            for col in range(n):
                r_diagonal = row - col
                l_diagonal = row + col
                
                if col in cols or r_diagonal in RD or l_diagonal in LD:
                    continue
                
                cols.append(col)
                LD.add(l_diagonal)
                RD.add(r_diagonal)

                backtrack(row + 1 , LD , RD , cols)

                cols.pop()
                LD.remove(l_diagonal)
                RD.remove(r_diagonal)
        res = []
        backtrack(0 , set() , set() , [])
        return res
        