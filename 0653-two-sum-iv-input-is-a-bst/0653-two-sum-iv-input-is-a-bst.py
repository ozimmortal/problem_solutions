# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findTarget(self, root: Optional[TreeNode], k: int) -> bool:

        nodes = []

        def dfs(node):

            if not node : return 

            dfs(node.left)
            nodes.append(node.val)
            dfs(node.right)
        dfs(root)

        l = 0
        r = len(nodes) - 1

        while l < r:
            s = nodes[l] + nodes[r]
            if s == k:
                return True
            elif s > k:
                r -= 1
            else:
                l += 1
        return False
        