class Solution:
    def nearestExit(self, maze: List[List[str]], entrance: List[int]) -> int:

        def check(x , y):
            return x == 0 or x == m - 1 or y == 0 or y == n - 1
        def valid(x , y):
            return 0 <= x < m and 0 <= y < n

        m , n = len(maze) , len(maze[0]) 
        queue = deque([(entrance[0] , entrance[1], 0)])
        seen = set(tuple(entrance))
        directions = [(1, 0), (0,1), (-1 , 0) , (0 ,-1)]
        
        while queue:
            x ,y , s = queue.popleft()
            if check(x ,y) and [x ,y] != entrance:
                return s
            for dx ,dy in directions:
                nx ,ny  = x + dx , y + dy
                if valid(nx ,ny) and (nx ,ny) not in seen and maze[nx][ny] == ".":
                    queue.append((nx ,ny , s + 1))
                    seen.add((nx ,ny))
        return -1
            



        