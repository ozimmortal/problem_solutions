class Solution:
    def minimumEffortPath(self, heights: List[List[int]]) -> int:
        
        def valid(r , c):
            return 0 <= r <= n-1 and 0 <= c <= m-1
        def check(effort):

            directions = [( 0 ,1) , (1 , 0) , (-1 , 0) , ( 0 , -1)]
            seen = {(0 , 0)}
            stack = [(0 , 0)]

            while stack:

                row , col = stack.pop()

                if (row , col) == (n - 1 , m - 1):
                    return True
                for dx , dy in directions:
                    nr , nc = row + dx , col + dy
                    if valid(nr,nc) and (nr , nc ) not in seen:
                        if abs(heights[nr][nc] - heights[row][col]) <= effort:
                            seen.add((nr , nc))
                            stack.append((nr , nc))
            return False
        
        n = len(heights)
        m = len(heights[0])

        l = 0
        r = max(max(row) for row in heights)

        while l <= r:
            mid = (l + r) // 2
            if check(mid):
                r = mid - 1
            else:
                l = mid + 1
        return l


        