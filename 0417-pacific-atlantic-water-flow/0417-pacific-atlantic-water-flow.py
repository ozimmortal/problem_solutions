class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        
        def valid(x , y):
            return 0 <= x < m and 0 <= y < n

        def dfs(x , y , seen):
            nonlocal a , p

            if x == 0 or y == 0 :
                p = True
            if x == m - 1 or y == n -1:
                a = True
            if p and a:
                return 

            directions = [(1 , 0), (0 , 1), (-1 , 0), (0, -1)]
            for dx , dy in directions:
                nx , ny = x + dx , y +  dy
                if valid(nx , ny) and (nx ,ny) not in seen and heights[x][y] >= heights[nx][ny]:
                    seen.add((nx ,ny))
                    dfs(nx , ny ,seen)
                
            
        
        m , n = len(heights) , len(heights[0])
        res = []
        
        for r in range(m):
            for c in range(n):
                p , a = False , False
                dfs(r ,c, set((r ,c)))
                if p and a:
                    res.append([r ,c])
        return res
        