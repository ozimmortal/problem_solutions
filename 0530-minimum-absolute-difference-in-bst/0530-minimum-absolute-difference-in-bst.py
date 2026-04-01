# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def getMinimumDifference(self, root: Optional[TreeNode]) -> int:
        m = float('inf')
        res = []
        def dfs(node):

            if not node: return

            dfs(node.left )
            res.append(node.val)
            dfs(node.right )

        dfs(root )
        print(res)
        for i in range(1,len(res)):
           
            m = min(m, abs(res[i] - res[i - 1]))
        return m

            