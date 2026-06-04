class Solution:
    def countAsterisks(self, s: str) -> int:
        stack = []
        border = 0

        for ch in s:
            if ch == "|":
                border += 1
                continue
        
            if border % 2 == 0:
                stack.append(ch)

        return stack.count("*")
            
        