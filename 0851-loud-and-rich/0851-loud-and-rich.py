class Solution:
    def loudAndRich(self, richer: List[List[int]], quiet: List[int]) -> List[int]:

        graph = defaultdict(list)
        for a , b in richer:
            graph[b].append(a)
        
        def dfs(node):
            if ans[node] != -1:
                return ans[node]
                
            best = node
            for n in graph[node]:
                person = dfs(n)
                if quiet[person] < quiet[best]:
                    best = person
            ans[node] = best
            return best
        ans = [-1] * len(quiet)

        for i in range(len(quiet)):
            if ans[i] == -1:
                ans[i] = dfs(i)
        return ans

        