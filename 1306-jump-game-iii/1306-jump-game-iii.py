class Solution:
    def canReach(self, arr: List[int], start: int) -> bool:
        
        def neighbour(node):
            left , right = node - arr[node] , node + arr[node]
            ans = []
            if 0 <= left <len(arr):
                ans.append(left)
            if 0 <= right < len(arr):
                ans.append(right)
            return ans
        
        seen = {start}
        def dfs(node):
            if arr[node] == 0: return True

            for n in neighbour(node):
                if n not in seen:
                    seen.add(n)
                    if dfs(n): return True
            return False
        
        return dfs(start)


        