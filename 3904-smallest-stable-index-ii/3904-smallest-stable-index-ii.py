class Solution:
    def firstStableIndex(self, nums: list[int], k: int) -> int:
        n = len(nums)
        prefixMax = [nums[0]]
        for i in range(1, n):
            prefixMax.append(max(prefixMax[-1] , nums[i]))
        
        suffixMin = [0] * n
        suffixMin[-1] = nums[-1]
        for i in range(n - 2 , -1 , -1):
            suffixMin[i] = min(nums[i] , suffixMin[i + 1])
        
        ints = []
        ans = -1
        for i in range(n):
            ins = prefixMax[i] - suffixMin[i]
            if ins <= k:
                if ans == -1 :
                    ans = i
                elif   ints[ans] > ins:
                    ans = min(ans , i)
            ints.append(ins)
        
        return ans
