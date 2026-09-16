class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        
        freq = defaultdict(int)
        l, ans = 0 , 0
        for r in range(len(s)):
            freq[s[r]] += 1

            while len(freq) != r - l + 1:
                freq[s[l]] -= 1
                if freq[s[l]] == 0:
                    del freq[s[l]]
                l += 1
            ans = max(ans , r - l + 1)
        
        return ans



