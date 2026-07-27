class Solution:
    def numOfSubarrays(self, arr: List[int], k: int, threshold: int) -> int:
        
        
        
        left , currSum = 0 , 0
        ans = 0
        for num in arr[:k]:
            currSum += num
        
        if currSum / k >= threshold:
            ans += 1

        for i in range(k , len(arr)):
            currSum += arr[i] - arr[left]
            left += 1

            if currSum / k >= threshold:
                ans += 1

        return ans
