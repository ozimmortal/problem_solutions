class Solution:
    def findCommonResponse(self, responses: List[List[str]]) -> str:

        c = defaultdict(int)

        for res in responses:
            for r in set(res):
                c[r] += 1
        
        m = [0,""]

        for k in c:
            if c[k] > m[0]:
                m[0] = c[k]
                m[1] = k
            elif c[k] == m[0]:
                if k < m[1]:
                    m[1] = k
        return m[1]


        