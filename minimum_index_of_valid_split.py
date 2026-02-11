class Solution:
    def minimumIndex(self, nums: List[int]) -> int:
        right = Counter(nums)
        left = defaultdict(int)
        n = len(nums) 
        for i in range(n - 1):
            left[nums[i]] += 1
            right[nums[i]] -= 1

            if left[nums[i]] >( 1 + i) /2 and right[nums[i]] > (n - 1 - i)/2:
                return i
        return -1
        