class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:

        res = []
        target = len(graph) - 1

        def backtrack(curr , i):
            nonlocal target
            if curr[-1] == target:
                res.append(curr[:])
                return
            
            for n in graph[i]:
                curr.append(n)
                backtrack(curr , n)
                curr.pop()

        backtrack([0] , 0)
        return res
            
            

        