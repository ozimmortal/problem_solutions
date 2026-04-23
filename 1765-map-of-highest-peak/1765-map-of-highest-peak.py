class Solution:
    def highestPeak(self, isWater: List[List[int]]) -> List[List[int]]:
        
        def valid(x , y):
            return 0 <= x < m and 0 <= y < n 
        
        queue = deque()
        seen = set()
        m , n = len(isWater) , len(isWater[0])
        directions = [(1,0),(0 , 1) , (-1, 0 ),(0 , -1)]

        for row in range(m):
            for col in range(n):
                if isWater[row][col] == 1:
                    queue.append((row ,col , 0))
                    seen.add((row, col))
                    isWater[row][col] = 0
        
        while queue:
            
            x , y , s = queue.popleft()
            for dx , dy in directions:
                nx , ny = x + dx , y + dy
                if valid(nx , ny) and (nx , ny) not in seen:
                    queue.append((nx , ny , s + 1))
                    seen.add((nx , ny))
                    isWater[nx][ny] = s + 1
        return isWater

        