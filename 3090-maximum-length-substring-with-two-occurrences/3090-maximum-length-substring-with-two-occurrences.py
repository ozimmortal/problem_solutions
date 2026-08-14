class Solution:
    def maximumLengthSubstring(self, s: str) -> int:
        
        left = 0
        cnt = defaultdict(int)
        ans = 0
        for right in range(len(s)):
            cnt[s[right]] += 1

            while max(cnt.values()) > 2:
                cnt[s[left]] -= 1
                left += 1
            
            ans = max(ans , right - left + 1)
        
        return ans
        