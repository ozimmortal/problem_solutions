# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:

        def dfs(root , s):

            if not root : return False

            if not root.left and not root.right:
                return (s + root.val ) == targetSum
                     
            l = dfs(root.left , s + root.val)
            r = dfs(root.right , s + root.val)

            return l or r
        
        return dfs(root,0)
