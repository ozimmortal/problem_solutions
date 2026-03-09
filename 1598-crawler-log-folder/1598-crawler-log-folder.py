class Solution:
    def minOperations(self, logs: List[str]) -> int:
        stack = []

        for p in logs:
            if p == "../" and stack:
                stack.pop()
                continue
            if p == "../" or p== "./":
                continue
            stack.append(p)
        return len(stack)