class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        graph = defaultdict(dict)
        for i in range(len(equations)):
            numerator , denominator = equations[i]
            value = values[i]
            graph[numerator][denominator] = value
            graph[denominator][numerator] = 1 / value

        
        def dfs(start , end):

            if start not in graph: return -1

            stack = [(start , 1)]
            seen = {start}

            while stack:
                node , val = stack.pop()

                if node == end: return val
                for n in graph[node]:
                    if n not in seen:
                        stack.append((n , graph[node][n] * val))
                        seen.add(n)
            return -1
        
        res = []
        for numerator , denominator in queries:
            res.append(dfs(numerator  , denominator))
        return res


        