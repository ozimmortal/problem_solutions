class Solution:
    def buildMatrix(self, k: int, rowConditions: List[List[int]], colConditions: List[List[int]]) -> List[List[int]]:
        res = [[0] * k for _ in range(k)]
        row_graph , col_graph = defaultdict(list) , defaultdict(list)
        row_indegree , col_indegree = [0] * (k + 1) , [0] * (k + 1)
        for x , y in rowConditions: 
            row_graph[x].append(y)
            row_indegree[y] += 1
        for x , y in colConditions: 
            col_graph[x].append(y)
            col_indegree[y] += 1
        
        def topo_sort(graph , indegree):

            order = []
            queue = deque([i for i in range(1, k+1) if indegree[i] == 0])
            while queue:
                node = queue.popleft()
                order.append(node)

                for n in graph[node]:
                    indegree[n] -= 1
                    if indegree[n] == 0:
                        queue.append(n)
            
            return order
        
        row_order , col_order = topo_sort(row_graph , row_indegree) ,topo_sort(col_graph , col_indegree)
        
        if len(row_order) != k or len(col_order) != k:
            return []
            
        placement = defaultdict(list)
        for i in range(k):
            placement[row_order[i]].append(i)
        for i in range(k):
            placement[col_order[i]].append(i)

        for k in placement:
            x , y = placement[k]
            res[x][y] = k
        return res
                

        