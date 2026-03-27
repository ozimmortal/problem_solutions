# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minDepth(self, root: Optional[TreeNode]) -> int:

        def dfs(root):
            if not root: return 0


            l = self.minDepth(root.left ) + 1
            r = self.minDepth(root.right) + 1 

            if l - 1  == 0:
                return r
            if r - 1 == 0:
                return l
            
            return  min(l, r)
        return dfs(root)

