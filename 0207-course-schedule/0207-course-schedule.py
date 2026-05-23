class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        
        graph = defaultdict(list)
        for x , y in prerequisites:
            graph[x].append(y)
        
        def dfs(node):
            if not self.no_cycle: return
            color[node] = GRAY
            for neighbour in graph[node]:
                if color[neighbour] == WHITE:
                    dfs(neighbour)
                elif color[neighbour] == GRAY:
                    self.no_cycle= False
            color[node] = BLACK
        
        WHITE , GRAY , BLACK = -1 , 0 , 1
        color = [WHITE for _ in range(numCourses)]
        self.no_cycle = True

         
        for x in range(numCourses):
            if color[x] == WHITE:
                dfs(x)
            if not self.no_cycle: return False
        return True
