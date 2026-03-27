# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        c = 0
        def dfs(node,ms):

            nonlocal c

            if not node : return 0

            if node.val >= ms:
                c += 1
            
            l = dfs(node.left , max(ms,node.val))
            r = dfs(node.right , max(ms,node.val))
        
        dfs(root, float('-inf'))
        return c




        