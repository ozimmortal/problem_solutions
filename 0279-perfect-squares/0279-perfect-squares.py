class Solution:
    def numSquares(self, n: int) -> int:
        
        def perfect_squares():
            t = []
            for i in range(1 , n + 1):
                sq = int(math.sqrt(i))
                if i == sq * sq:
                    t.append(i)
            return t

        squares = perfect_squares()
        queue = deque([(0, 0)])
        seen = set()

        while queue:
            node , step = queue.popleft()
            if node == n:
                return step

            for ne in squares:
                nxt = node + ne
                if nxt <= n and nxt not in seen :
                    queue.append((nxt , step + 1))
                    seen.add(nxt)
        
        


