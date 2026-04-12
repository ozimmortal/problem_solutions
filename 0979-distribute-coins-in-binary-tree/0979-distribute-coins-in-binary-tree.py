# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def distributeCoins(self, root: Optional[TreeNode]) -> int:
        res  = 0
       

        def dfs(node):
            nonlocal res

            if not node: return 0

            lc = dfs(node.left)
            rc = dfs(node.right)

            cc = node.val - 1 + lc + rc
            res += abs(cc)
            return cc
        dfs(root)
        return res