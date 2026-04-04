# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        res = []

        def dfs(node , comb):

            if not node: return
            
            comb.append(node.val)

            if (not node.left and not node.right) and sum(comb) == targetSum:
                res.append(comb[:])

            dfs(node.left , comb)
            dfs(node.right , comb)

            comb.pop()

        dfs(root , [])
        return res
            

            
        