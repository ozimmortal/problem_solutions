"""
# Definition for Employee.
class Employee:
    def __init__(self, id: int, importance: int, subordinates: List[int]):
        self.id = id
        self.importance = importance
        self.subordinates = subordinates
"""

class Solution:
    def getImportance(self, employees: List['Employee'], id: int) -> int:

        graph = defaultdict(list)
        for employee in employees:
            graph[employee.id] = [employee.importance , employee.subordinates]
        
        def dfs(node):
            importance , subordinates = graph[node]
            self.total += importance

            for sub in subordinates:
                dfs(sub)
        self.total = 0
        dfs(id)
        return self.total
        