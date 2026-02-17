class Solution:
    def flipAndInvertImage(self, image: List[List[int]]) -> List[List[int]]:
        res = []

        for r in image:
            temp = []
            for re in r[::-1]:
                if re == 0 :
                    temp.append(1)
                else:
                    temp.append(0)
            res.append(temp)
        return res
        