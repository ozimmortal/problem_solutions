# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxLevelSum(self, root: Optional[TreeNode]) -> int:
        
        queue = deque([root])
        res = [root.val , 0]
        level = 0
        while queue:

            n = len(queue)
            temp = 0
            for _ in range(n):
                node  = queue.popleft()
                temp+=node.val

                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)

            if temp >  res[0]:
                res = [temp , level]
            elif temp == res[0]:
                res = [temp , min(res[1],level)]
            level += 1
        return res[1] + 1