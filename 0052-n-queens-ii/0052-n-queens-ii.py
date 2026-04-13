class Solution:
    def totalNQueens(self, n: int) -> int:
        
        def backtrack(row ,LD , RD , cols):

            if row == n:
                return 1

            ans = 0

            for col in range(n):
                r_diagonal = row - col
                l_diagonal = row + col
                
                if col in cols or r_diagonal in RD or l_diagonal in LD:
                    continue
                
                cols.add(col)
                LD.add(l_diagonal)
                RD.add(r_diagonal)

                ans += backtrack(row + 1 , LD , RD , cols)

                cols.remove(col)
                LD.remove(l_diagonal)
                RD.remove(r_diagonal)

            return ans
        return backtrack(0 , set() , set() ,set())
