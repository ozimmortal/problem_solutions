class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        
        N = 9
        for x in range(N):
            seen = set()
            for r in range(N):
                num = board[r][x]
                if num in seen:
                    return False
                if num != ".":
                    seen.add(num)
            
            seen = set()
            for c in range(N):
                num = board[x][c]
                if num in seen:
                    return False
                if num != ".":
                    seen.add(num)

        seen = defaultdict(set)
        for r in range(N):
            for c in range(N):
                num = board[r][c]
                nr , nc = r // 3, c//3
                if num in seen[(nr , nc)]:
                    return False

                if num != ".":
                    seen[(nr, nc)].add(num)

        return True
                

        




     

        