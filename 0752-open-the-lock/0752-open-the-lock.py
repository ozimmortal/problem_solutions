class Solution:
    def openLock(self, deadends: List[str], target: str) -> int:
        
        def neighbors(node):
            ans = []
            for i in range(4):
                num = int(node[i])
                for change in [-1, 1]:
                    x = (num + change) % 10
                    ans.append(node[:i] + str(x) + node[i + 1:])
            return ans
        
        if "0000" in deadends:
            return -1
        
        queue = deque([("0000" , 0)])
        seen = set(deadends)
        seen.add("0000")

        while queue:
            node , step = queue.popleft()
            if node == target:
                return step
            
            for n in neighbors(node):
                if n not in seen:
                    queue.append((n , step + 1))
                    seen.add(n)
        return -1
            