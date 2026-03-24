# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def goodNodes(self, root: TreeNode) -> int:

        def dfs(root,tg):

            if not root: return 0
            
            l = dfs(root.left , max(tg , root.val))
            r = dfs(root.right ,max(tg,root.val))

            g = l + r

            if root.val >= tg:
                g += 1

            return g
        return dfs(root,float('-inf'))



        