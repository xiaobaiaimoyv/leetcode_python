class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        ans = 0
        def dfs(node: Optional[TreeNode], x: int) -> None:
            if node is None:
                return
            x = x * 10 + node.val
            if node.left is None and node.right is None:  # node 是叶子节点
                nonlocal ans
                ans += x
                return
            dfs(node.left, x)
            dfs(node.right, x)
        dfs(root, 0)
        return ans

