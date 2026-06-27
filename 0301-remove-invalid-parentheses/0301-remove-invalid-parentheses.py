class Solution:
    def removeInvalidParentheses(self, s: str) -> List[str]:
        
        def valid(p):
            stack = []
            for ch in p:
                if ch == "(":
                    stack.append(ch)
                elif ch == ")":
                    if stack and stack[-1] == "(":
                        stack.pop()
                    else:
                        if ch == ")":
                            stack.append(ch)
            return not stack
        

        queue = deque([s])
        seen = {s}
        res = []

        while queue:
            node = queue.popleft()
            if valid(node):
                if len(res) == 0 or (len(res) > 0  and len(res[-1]) == len(node)) :
                    res.append(node)
                else:
                    break

            n = len(node)
            for i in range(n):
                if node[i] == "(" or node[i] == ")":
                    new_node = node[:i] + node[i + 1: ]
                    if new_node not in seen:
                        seen.add(new_node)
                        queue.append(new_node)
        
        return res if res else [""]
