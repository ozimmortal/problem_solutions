class Solution:
    def minLights(self, lights: list[int]) -> int:
        n = len(lights)

        covered = [0] * n
        
        right = -1
        for i in range(n):
            v = lights[i]
            if v != 0:
                right = max(right, min(n - 1 , i + v))
            
            if i <= right:
                covered[i] = 1
        
        left = n + 1
        for i in range(n-1 , -1 , -1):
            v = lights[i]
            if v != 0:
                left = min(left, max(0 , i - v))
            
            if i >= left:
                covered[i] = 1

        ans , cnt = 0 , 0
        for i in range(n):
            if covered[i] == 0:
                cnt += 1
            elif covered[i] == 1:
                ans += ceil(cnt / 3)
                cnt = 0
        ans += ceil(cnt / 3)
        return ans

                
        

