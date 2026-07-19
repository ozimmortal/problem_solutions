class Solution:
    def smallestSubsequence(self, s: str) -> str:
        
        cnt = Counter(s)
        stack = []
        seen = set()

        for ch in s:
            cnt[ch] -= 1
            if ch in seen:
                continue

            while stack and stack[-1] > ch and cnt[stack[-1]] > 0:
                rm = stack.pop()
                seen.remove(rm)
            
            stack.append(ch)
            seen.add(ch)
        
        return "".join(stack)