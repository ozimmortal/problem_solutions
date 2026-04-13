# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def constructMaximumBinaryTree(self, nums: List[int]) -> Optional[TreeNode]:
        
        def backtrack(nums):
            if not nums: return 

            idx = nums.index(max(nums))
            node = TreeNode(nums[idx])

            node.left = backtrack(nums[0 : idx])
            node.right = backtrack(nums[idx + 1:])

            return node
        
        return backtrack(nums)