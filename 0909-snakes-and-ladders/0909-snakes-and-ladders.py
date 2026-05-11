class Solution:
    def snakesAndLadders(self, board: List[List[int]]) -> int:
        
        def  find_pos(num):
            t = (num - 1) // n
            x = n - t - 1
            y = (num - 1) % n if t % 2 == 0 else n - 1 - (num - 1) % n
            return x, y
        
        n = len(board)
        queue= deque([(1 , 0)])
        seen = {1}
        while queue:
            curr , s = queue.popleft()
            if curr == n *n:
                return s
            for r in range(1 , 7):
                next_move = curr + r
                if next_move > n * n:
                    break
                x , y = find_pos(next_move)
                if board[x][y] != - 1:
                    next_move = board[x][y]

                if next_move not in seen:
                    seen.add(next_move)
                    queue.append((next_move, s + 1))
        return -1 