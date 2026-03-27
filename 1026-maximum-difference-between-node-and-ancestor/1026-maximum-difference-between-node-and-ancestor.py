# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxAncestorDiff(self, root: Optional[TreeNode]) -> int:

        md = 0

        def dfs(root , ma, mi):
            nonlocal md
            if not root : return 

            if root.val < mi:
                mi = root.val
            if root.val > ma:
                ma = root.val

            if ma > mi:
                md = max(md,abs(ma-mi))

            dfs(root.left , ma , mi)
            dfs(root.right , ma, mi)
        dfs(root,0,10**5)
        return md 


        