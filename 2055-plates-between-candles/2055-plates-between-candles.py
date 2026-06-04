class Solution:
    def platesBetweenCandles(self, s: str, queries: List[List[int]]) -> List[int]:
        
        prefix = [1 if s[0] == "*" else 0]
        for i in range(1 ,len(s)):
            prefix.append(prefix[i - 1] + (1 if s[i] == "*" else 0)  )
        
        left = [-1] * len(s)
        last = -1

        for i in range(len(s)):
            if s[i] == "|":
                last = i
            left[i] = last
        
        right = [-1] * len(s)
        last = -1

        for i in range(len(s) - 1 , -1 , -1):
            if s[i] == "|":
                last = i
            right[i] = last
        
        ans = []
        for l , r in queries:
            start = right[l]
            end = left[r]

            if start == -1 or end == -1 or start >= end:
                ans.append(0)
            else:
                ans.append(prefix[end] - prefix[start])
        return ans
