# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isEvenOddTree(self, root: Optional[TreeNode]) -> bool:
        
        # conditions
        # for every even indexed all the node values must be odd
        # for every odd indexed all the node values must be even

        queue = deque([root])
        level = 0

        while queue:

            n = len(queue)
            t = []
            for _ in range(n):
                node = queue.popleft()
                # check for parity and strict monotonicity
                # even indexed
                if level % 2 == 0:
                    if node.val % 2 == 0 or (t and  node.val <= t[-1]):
                        return False
                # odd indexed
                if level % 2 == 1:
                    if node.val %2 == 1 or (t and node.val >= t[-1]):
                        return False
                
                t.append(node.val)
                if node.left: queue.append(node.left)
                if node.right: queue.append(node.right)

            level += 1
        
        return True



