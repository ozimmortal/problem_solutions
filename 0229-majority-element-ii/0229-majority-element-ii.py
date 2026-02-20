from collections import Counter

class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        counter = Counter(nums) # count the frequency of the element 
        target = len(nums) / 3
        result = []

        for k in counter:
            if counter[k] > target:
                result.append(k)
        return result