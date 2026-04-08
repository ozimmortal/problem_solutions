# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def closestNodes(self, root: Optional[TreeNode], queries: List[int]) -> List[List[int]]:
        nums = []
        def dfs(node):
            if not node: return 

            dfs(node.left)
            nums.append(node.val)
            dfs(node.right)
        dfs(root)
        print(nums)
        res = []
        for n in queries:
            i , j = bisect_right(nums, n) - 1 , bisect_left(nums, n)
            x = nums[i] if i >= 0 else -1
            y = nums[j] if j < len(nums) else -1
            res.append([x,y])
        return res

