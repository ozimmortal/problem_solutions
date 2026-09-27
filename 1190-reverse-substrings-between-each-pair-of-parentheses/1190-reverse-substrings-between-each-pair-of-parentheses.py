class Solution:
    def reverseParentheses(self, s: str) -> str:
        
        chars = [''] * len(s)
        par = []

        for i, ch in enumerate(s):
            if ch == "(":
                par.append(i)
            elif ch == ")":
                left , right = par.pop() + 1, i - 1
                while left < right:
                    chars[left], chars[right] = chars[right] , chars[left]
                    left += 1
                    right -= 1
            else:
                chars[i] = ch

        return "".join(chars) 
