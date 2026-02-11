class Solution:
    def frequencySort(self, s: str) -> str:
        c = Counter(s)
        o = defaultdict(list)
        result =  ''
        highest = 0
        for k in c.keys():
            o[c[k]].append(k)
        for i in sorted(o.keys(),reverse=True):
            for j in o[i]:
                result += j*i
        return result
        