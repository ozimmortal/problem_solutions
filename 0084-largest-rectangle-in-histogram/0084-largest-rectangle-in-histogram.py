class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack = [ ]
        ans = float('-inf')
        n = len(heights)

        for i in range(n):
            idx = i
            while stack and stack[-1][0] > heights[i]:
                h , idx = stack.pop()
                ans = max(ans , h * (i - idx))
            stack.append([heights[i], idx])
        
        while stack:
            h , idx = stack.pop()
            ans = max(ans , h * (n - idx))
        return ans

