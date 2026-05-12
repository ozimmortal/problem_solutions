class Solution:
    def maximumDetonation(self, bombs: List[List[int]]) -> int:
        
        graph = defaultdict(list)
        for i in range(len(bombs)):
            xi , yi , ri = bombs[i]

            for j in range(len(bombs)):
                xj , yj , rj = bombs[j]
                d = math.sqrt((xi - xj)**2 + (yi - yj) ** 2)
                if d <= ri:
                    graph[(xi , yi , ri )].append(j)
        
        def dfs(node , seen):
            c = 0
            for i in graph[node]:
                n = bombs[i]
                if i not in seen:
                    seen.add(i)
                    c += dfs(tuple(n) , seen) +  1
            return c
        ans = 1
        for i , node in enumerate(bombs):
            c =  dfs(tuple(node) , set())
            ans = max(ans , c)
        return ans

