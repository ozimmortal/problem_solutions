class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:

        n = 9
        # check row
        for r in range(n):
            seen = set()
            for val in board[r]:
                if val in seen:
                    print("R" , val)
                    return False
                if val != ".":
                    seen.add(val)

        # check column
        for c in range(n):
            seen = set()
            r=0
            while r < n:
                val = board[r][c]
                if val in seen:
                    print("C")
                    return False
                if val != ".":
                    seen.add(val)
                r += 1
        
        # check box
        seen = defaultdict(set)
        for r in range(n):
            for c in range(n):
                val = board[r][c]
                if val == ".":
                    continue
                nr , nc = r//3 , c//3
                if val in seen[(nr , nc)]:
                    print("B")
                    return False
                seen[(nr , nc)].add(val)
        return True

        




     

        