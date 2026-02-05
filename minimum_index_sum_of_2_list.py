class Solution:
    def findRestaurant(self, list1: List[str], list2: List[str]) -> List[str]:
        ci = {}
        cSum = {}
        mini = float('inf')
        ans = []
        for i, word in enumerate(list1):
            ci[word] = i
        for j , word in enumerate(list2):
            if word in ci:
                cSum[word] = ci[word] + j
                mini = min(mini , cSum[word])
        for k in cSum:
            if cSum[k] == mini:
                ans.append(k)
        return ans
        
        