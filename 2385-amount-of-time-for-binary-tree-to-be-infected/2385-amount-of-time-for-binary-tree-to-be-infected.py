# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def amountOfTime(self, root: Optional[TreeNode], start: int) -> int:
        
        self.target = None
        def find_target(node):
            if not node: return

            if node.val == start:
                self.target = node
                return
            find_target(node.left)
            find_target(node.right)
        
        find_target(root)

        def dfs(node , parent):
            if not node: return

            node.parent = parent
            dfs(node.left ,node)
            dfs(node.right , node)
        dfs(root, None)

        queue = deque([self.target])
        seen = {self.target.val}
        minute = 0

        while queue:
            l = len(queue)
            for _ in range(l):
                node = queue.popleft()
                for n in [node.left ,node.right , node.parent]:
                    if n and n.val not in seen:
                        queue.append(n)
                        seen.add(n.val)
            minute +=1
        return minute - 1
