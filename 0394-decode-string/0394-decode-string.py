class Solution:
    def decodeString(self, s: str) -> str:
        stack = []

        for ch in s:
            if ch != "]":
                stack.append(ch)
            else:
                ns = deque()
                while stack and stack[-1] != "[":
                    t = stack.pop()
                    ns.appendleft(t)
                
                stack.pop()

                am = ""
                while stack and stack[-1].isdigit():
                    am += stack.pop()
                
                stack.append("".join(ns) * int(am[::-1]))
        return "".join(stack)

        