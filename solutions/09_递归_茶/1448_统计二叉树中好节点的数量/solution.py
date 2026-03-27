# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def goodNodes(self, root: Optional[TreeNode]) -> int:
        count = 0

        def dfs(root, maxer):
            nonlocal count
            if not root:
                return
            if root.val >= maxer:
                count += 1
                maxer = root.val
            dfs(root.left, maxer)
            dfs(root.right, maxer)

        dfs(root, root.val)
        return count

