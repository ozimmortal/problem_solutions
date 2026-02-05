from collections import defaultdict
class Solution:
    def subdomainVisits(self, cpdomains: List[str]) -> List[str]:
        ans = []
        col = defaultdict(int)

        for d in cpdomains:
            s = d.split(" ")
            visits = int(s[0])
            domain = s[1]
            col[domain] += visits

            while domain.find(".") != -1:
                sub_d = domain[domain.find(".")+1:]
                col[sub_d] += visits
                domain = sub_d
        for k in col:
            ans.append(str(col[k]) + " " + k)

        return ans
            



        