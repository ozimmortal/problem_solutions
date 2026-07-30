class Solution:
   
    def solveSudoku(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        
        r , c , b = defaultdict(set),defaultdict(set),defaultdict(set)
        fill = []
        for x in range(9):
            for y in range(9):
                if board[x][y] == ".":
                    fill.append((x , y))
                else:
                    r[x].add(board[x][y])
                    c[y].add(board[x][y])
                    b[(x//3 , y//3)].add(board[x][y])

        def bt(s):
            if s == len(fill): return True
            
            x , y = fill[s]
            for i in range(1 , 10):
                val = str(i)
                if val not in r[x] and val not in c[y] and val not in b[(x//3,y//3)]:
                    board[x][y] = val
                    _ = r[x].add(val) , c[y].add(val), b[(x//3,y//3)].add(val)
                    if bt(s + 1): return True
                    _ = r[x].remove(val) , c[y].remove(val), b[(x//3,y//3)].remove(val)
                    board[x][y] = "."

            return False
        bt(0)
                



                
    









            

        