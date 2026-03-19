class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        res = [[1]]

        for i in range(rowIndex):
            row = []
            t = [0] + res[-1] + [0]
            for j in range(len(res[-1]) + 1):
                row.append(t[j] + t[j + 1])
            res.append(row)
        return res[-1]