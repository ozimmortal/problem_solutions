class Solution:
    def findRotation(self, mat: list[list[int]], target: list[list[int]]) -> bool:
        c = 0
        n = len(mat)

        if mat == target : return True

        while c < 3:
            mat = [list(e[::-1]) for e in zip(*mat)]

            if mat == target :
                return True
            c += 1

        return False