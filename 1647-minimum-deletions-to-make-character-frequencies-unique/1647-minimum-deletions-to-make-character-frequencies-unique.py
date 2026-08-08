class Solution:
    def minDeletions(self, s: str) -> int:
        
        freq = [0] * 26
        for ch in s:
            freq[ord(ch) - ord('a')] += 1
        
        freq.sort(reverse=True)
        ans = 0
        for i in range(26):
            f = freq[i]
            freq[i] = 0
            while f > 0 and f in freq:
                f -= 1
                ans += 1
            freq[i] = f
            
        
        return ans
            
