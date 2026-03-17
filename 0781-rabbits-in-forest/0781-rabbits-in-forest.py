class Solution:
    def numRabbits(self, answers: List[int]) -> int:
        res = 0
        c = Counter(answers)
        for k in c:
            res += (k + 1) * math.ceil(c[k] / (k + 1))
        return res
        