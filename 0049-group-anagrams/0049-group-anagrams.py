class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        coll = defaultdict(list)
        for word in strs:
            k = "".join(sorted(word))
            coll[k].append(word)
        return [v for v in coll.values()]


