class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        
        graph = defaultdict(list)
        indegree = [0] * numCourses
        for x , y in prerequisites:
            graph[y].append(x)
            indegree[x] += 1

        queue = deque([i  for i in range(numCourses) if indegree[i] == 0])
        courses = []
        while queue:
            course = queue.popleft()
            courses.append(course)

            for dep in graph[course]:
                indegree[dep] -= 1
                if indegree[dep] == 0:
                    queue.append(dep)
        
        return courses if len(courses) == numCourses else []
