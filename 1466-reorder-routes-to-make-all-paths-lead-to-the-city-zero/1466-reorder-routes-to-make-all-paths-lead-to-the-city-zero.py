class Solution:
    def minReorder(self, n: int, connections: List[List[int]]) -> int:
        
        g = defaultdict(list)
        r = set()
        for x , y in connections:
            g[x].append(y)
            g[y].append(x)
            r.add((x,y))
        
        def dfs(node):
            ans = 0

            for n in  g[node]:
                pair = (node , n)
                if n not in seen:
                    if pair in r:
                        ans += 1
                    seen.add(n)
                    ans += dfs(n)
            return ans
        
        seen = {0}
        return dfs(0)

        