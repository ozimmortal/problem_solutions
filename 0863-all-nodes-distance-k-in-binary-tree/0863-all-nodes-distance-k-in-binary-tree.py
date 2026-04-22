# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def distanceK(self, root: TreeNode, target: TreeNode, k: int) -> List[int]:
        
        def dfs(node , parent):
            if not node: return 

            node.parent = parent
            dfs(node.left , node)
            dfs(node.right , node)
        
        dfs(root , None)

        queue = deque([target])
        seen = {target.val}
        d = 0

        while queue and d < k:
            l = len(queue)
            for _ in range(l):
                node = queue.popleft()
                for n in [node.left , node.right , node.parent]:
                    if n and n.val not in seen:
                        queue.append(n)
                        seen.add(n.val)
            d += 1
        return [n.val for n in queue]