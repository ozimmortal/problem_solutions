class Solution:
    def jump(self, nums: List[int]) -> int:
        n = len(nums)
        queue = deque([(0 , nums[0] , 0)])
        seen = {0}
        while queue:
            i , j , s = queue.popleft()
            
            if i == n - 1:
                return s
            
            for j in range(1 , j+1):
                k = i + j
                if i + j < n and k not in seen:
                    queue.append((k, nums[k] , s + 1))
                    seen.add(k)
        