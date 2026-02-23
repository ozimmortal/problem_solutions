class Solution:
    def dividePlayers(self, skill: List[int]) -> int:
        skill.sort()

        res = 0
        tra = 0
        l , r = 0 , len(skill) - 1

        while l < r:
            t = skill[l] + skill[r]
            if res and tra != t:
                return -1
            tra = t
            res += skill[l] * skill[r]

            l += 1
            r -= 1
        return res

