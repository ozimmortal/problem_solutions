# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deepestLeavesSum(self, root: Optional[TreeNode]) -> int:
        q = deque([root])
        height = 0
        while q:
            n = len(q)
            for i in range(n):
                node = q.popleft()
        
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
            height += 1
        
        q = deque([root])
        res = 0

        while height - 1 > 0:
            n = len(q)
            for _ in range(n):
                node = q.popleft()
        
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
            height -= 1
        
        for node in q:
            res += node.val
        return res