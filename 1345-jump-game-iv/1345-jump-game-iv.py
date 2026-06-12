class Solution:
    def minJumps(self, arr: List[int]) -> int:
        
        graph = defaultdict(list)
        n = len(arr)
        for i in range(n):
            graph[arr[i]].append(i)
        
        queue = deque([(0 , 0)])
        seen = {0}
        while queue:
            idx , step = queue.popleft()

            if idx == n - 1:
                return step

            num = arr[idx]
            for node in graph[num]:
                if node not in seen:
                    queue.append((node , step+1))
                    seen.add(node)
            if num in graph:
                del graph[num]
            
            left , right = idx - 1 , idx + 1
            if left >= 0 and left not in seen:
                queue.append((left , step + 1))
                seen.add(left)

            if right < n and right not in seen:
                queue.append((right , step + 1))
                seen.add(right)
        return -1
