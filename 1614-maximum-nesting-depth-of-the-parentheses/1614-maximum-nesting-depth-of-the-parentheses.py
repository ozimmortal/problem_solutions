class Solution:
    def maxDepth(self, s: str) -> int:
        
        ans = 0
        stack = []

        for i , ch in enumerate(s):
            if ch == "(":
                stack.append(i)
            elif ch == ")":
                ans=  max(ans, len(stack))
                stack.pop()
        
        return ans