class Solution:
    def largestInteger(self, nums: List[int], k: int) -> int:
        

        counter = defaultdict(int)
        for i in range(len(nums) - k + 1):
            for n in set(nums[i: i + k]):
                counter[n] += 1
        
        ans = -1
        for k , val in counter.items():
            if val == 1:
                ans = max(ans , k)
            
        return ans