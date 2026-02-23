class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        l = 0
        r = len(numbers) -1 
        while l < r:
            two_sums = numbers[l] + numbers[r]
            if two_sums == target:
                return [l+1,r + 1]
            elif two_sums > target:
                r -= 1
            else:
                l += 1
        

        