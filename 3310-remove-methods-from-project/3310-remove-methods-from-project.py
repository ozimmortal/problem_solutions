class Solution:
    def remainingMethods(self, n: int, k: int, invocations: List[List[int]]) -> List[int]:
        
        graph = defaultdict(list)
        indegree = [0] * n
        for a , b in invocations:
            graph[a].append(b)
            indegree[b] +=1
        
        def dfs(node):
            for nei in graph[node]:
                indegree[nei] -= 1
                if nei not in seen:
                    seen.add(nei)
                    dfs(nei)
        
        seen = {k}
        dfs(k)
        
        
        rm = not any(indegree[s] > 0 for s in seen)
        res = []
        for i in range(n):
            if i in seen and rm:
                continue
            res.append(i)
        return res
