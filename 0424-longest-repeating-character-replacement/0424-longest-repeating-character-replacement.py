class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        freq = [0] * 26
        l , ans = 0 , 0

        for r in range(len(s)):
            idx = ord(s[r]) - ord('A')
            freq[idx] += 1

            while sum(freq) - max(freq) - k > 0:
                idx = ord(s[l]) - ord('A')
                freq[idx] -= 1
                l += 1
            
            ans = max(ans , r - l + 1)
        
        return ans

