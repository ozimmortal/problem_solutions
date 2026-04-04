# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def getAllElements(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> List[int]:
        
        res = []
        queue = deque([root1,root2])

        while queue:

            n  = len(queue)

            for _ in range(n):
                node  = queue.popleft()
                if node:
                    res.append(node.val)

                    if node.left : queue.append(node.left)
                    if node.right: queue.append(node.right)
        res.sort()
        return res