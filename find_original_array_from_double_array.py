class Solution:
    def findOriginalArray(self, changed: List[int]) -> List[int]:
        n = len(changed)
        if n  % 2 != 0:
            return []
        ans = []
        c = Counter(changed)

        for original in sorted(changed):
            doubled = original * 2

            if original in c and doubled in c:
                ans.append(original)

                c[original] -= 1
                c[doubled] -= 1

                if c[original] == 0:
                    del c[original]
                if c[doubled] == 0:
                    del c[doubled]
            
        if len(c) == 0:
            return ans
        else:
            return []
                


