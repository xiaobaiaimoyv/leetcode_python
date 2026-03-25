class Solution:
    def minDepth(self, root: Optional[TreeNode]) -> int:
        ans = inf
        def dfs(node: Optional[TreeNode], cnt: int) -> None:
            if node is None:
                return
            nonlocal ans
            cnt += 1
            if cnt >= ans:
                return  # 最优性剪枝
            if node.left is None and node.right is None:  # node 是叶子
                ans = cnt
                return
            dfs(node.left, cnt)
            dfs(node.right, cnt)
        dfs(root, 0)
        return ans if root else 0

