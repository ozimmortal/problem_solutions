class Solution:
    def checkIfPrerequisite(self, numCourses: int, prerequisites: List[List[int]], queries: List[List[int]]) -> List[bool]:
        

        graph = defaultdict(list)
        for pre , course in prerequisites:
            graph[course].append(pre)


        def dfs(node , target ):

            if node == target:
                return True

            for n in graph[node]:
                if n not in seen:
                    seen.add(n)
                    if dfs(n, target):
                        return True
            
            return False
        ans = []
        for pre , course in queries:
            seen = {course}
            ans.append(dfs(course , pre))
        return ans

            

            