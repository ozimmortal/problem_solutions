class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        res = [[1]]

        for i in range(numRows - 1):
            row = []
            t = [0] + res[-1] + [0]
            for j in range(len(res[-1]) + 1):
                row.append(t[j] + t[j + 1])
            res.append(row)
        return res
            