class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        
        graph = defaultdict(list)
        n = len(isConnected)
        for i in range(n):
            for j in range(n):
                if isConnected[i][j] == 1:
                    graph[i].append(j)
        
        def dfs(node):
            arr = graph[node]
            for n in arr:
                if n not in seen:
                    seen.add(n)
                    dfs(n)
        seen =set()
        res = 0

        for i in range(n):
            if i not in seen:
                dfs(i)
                res += 1
        return res
            