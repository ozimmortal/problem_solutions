class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        prefix = [nums[0]]

        for i in range(1,n):
            product = prefix[i - 1] * nums[i]
            prefix.append(product)
        
        suffix = [nums[-1]]

        for i in range(n - 2 , -1 , -1):
            product = suffix[n - i  - 2] * nums[i]
            suffix.append(product)
        
        suffix = suffix[::-1]
        print(prefix,suffix)
        result = [0] * n
        # for the first and last element
        result[0] = suffix[1]
        result[-1] = prefix[-2]
        #  for the middle element

        for i in range(1,n-1):
            result[i] = prefix[i-1] * suffix[i + 1]
        return result




        