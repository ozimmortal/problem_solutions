class Solution:
    def longestPalindrome(self, s: str) -> int:
        counts = Counter(s)
        n = len(s)

        t = 0 
        for key ,freq in counts.items():
            if freq % 2 == 0:
                t += freq
            else:
                t += freq - 1
        
        return t + 1 if t + 1 <= n else t
        