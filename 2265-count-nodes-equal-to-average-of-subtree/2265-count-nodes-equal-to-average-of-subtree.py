# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def averageOfSubtree(self, root: TreeNode) -> int:
        
        cnt = 0
        def dfs(node):
            nonlocal cnt
            if not node: return 0 , 0

            leftSum , leftCnt = dfs(node.left )
            rightSum , rightCnt = dfs(node.right)

            totalCnt, totalSum = leftCnt + rightCnt + 1 , leftSum + rightSum + node.val
            if node.val == ((totalSum // totalCnt) if totalCnt > 0 else 0) :
                cnt += 1
            
            return totalSum , totalCnt
        dfs(root)
        return cnt
            