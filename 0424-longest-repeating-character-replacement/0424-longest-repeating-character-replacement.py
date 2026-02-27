class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        c =  defaultdict(int)

        left , ans = 0 , 0

        for right in range(len(s)):

            c[s[right]] += 1

            while (right - left + 1) - max(c.values()) > k:
                c[s[left]] -= 1

                if c[s[left]] == 0:
                    del c[s[left]]

                left += 1

            ans = max(ans,right - left + 1)
        return ans


