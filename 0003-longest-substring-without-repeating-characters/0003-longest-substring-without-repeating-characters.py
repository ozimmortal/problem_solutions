from collections import defaultdict

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        left , ans = 0 ,0
        c = set()
        # for right in range(len(s)):
        #     c[s[right]] += 1
        #     while sum(c.values()) > len(c.keys()):
        #         c[s[left]] -= 1
        #         if c[s[left]] == 0:
        #             del c[s[left]]
        #         left += 1
            
        #     ans = max(ans , right -left + 1)
        # return ans

        for r , ch in enumerate(s):

            while ch  in  c:
                c.remove(s[left])
                left += 1
            c.add(ch)
            ans = max(ans,r-left + 1)

        return ans




