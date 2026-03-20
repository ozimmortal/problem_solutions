class Solution:
    def predictTheWinner(self, nums: List[int]) -> bool:
        
        def dfs(l , r):
            if l == r:
                return nums[l]
            
            left_pick = nums[l] - dfs(l + 1 , r)
            right_pick = nums[r] - dfs(l, r - 1)

            return max(left_pick , right_pick)

        return dfs(0 , len(nums)-1) >= 0