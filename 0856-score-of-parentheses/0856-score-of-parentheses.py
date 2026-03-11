class Solution:
    def scoreOfParentheses(self, s: str) -> int:
        stack = []
        ans, val = 0 , 0
        for c in s:
            if c == "(":
                stack.append(0)
            else:
                v = stack.pop()
                if v == 0:
                    val = 1
                else:
                    val = v * 2 

                if not stack:
                    ans += val
                else:
                    stack[-1] += val                
        return ans 

        