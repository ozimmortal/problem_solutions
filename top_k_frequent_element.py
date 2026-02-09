class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        c = Counter(nums)
        lst = [[value , key] for key, value in c.items()]
        lst.sort(reverse = True)
        return [lst[n][1] for n in range(k)]