class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        
        dic = defaultdict(int)
        for i , n in enumerate(nums):
            if n in dic and abs(i - dic[n]) <= k:
                return True
            
            dic[n] = i
        
        return False