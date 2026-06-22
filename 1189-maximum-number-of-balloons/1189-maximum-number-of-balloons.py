
from collections import Counter


class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        target = "balloon"
        b = Counter(target)
        d = Counter(text)
        ans = float('inf')
        
        for s in target:
            if s not in d:
                return 0
            count = d[s] // b[s]
            ans = min(ans,count)
        return ans