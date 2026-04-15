class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        
        c = Counter(nums)
        ans = [0 , 0]
        for i in range(1,len(nums)+1):
            if i not in c:
                ans[1] = i
                break
        for k in c:
            if c[k] == 2:
                ans[0] = k
                break

        return ans

        