class Solution:
    def removeDuplicateLetters(self, s: str) -> str:
        
        cnt , seen = Counter(s) , set()
        stack = []
        for ch in s:
            cnt[ch] -= 1
            
            if ch in seen: continue

            while stack and stack[-1] > ch and cnt[stack[-1]] > 0:
                seen.remove(stack.pop())

            stack.append(ch)
            seen.add(ch)
        
        return "".join(stack)
        