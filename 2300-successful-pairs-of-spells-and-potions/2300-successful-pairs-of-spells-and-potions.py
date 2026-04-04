from bisect import bisect_left
class Solution:
    def successfulPairs(self, spells: List[int], potions: List[int], success: int) -> List[int]:

        res = []
        potions.sort()
        for s in spells:
            t = math.ceil(success / s)
            i = bisect_left(potions , t)
            print(t , i)
            res.append(len(potions) - i)
        return res
        