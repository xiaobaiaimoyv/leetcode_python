class Solution:
    def goodNodes(self, root: TreeNode, mx=-inf) -> int:
        if root is None:
            return 0
        left = self.goodNodes(root.left, max(mx, root.val))
        right = self.goodNodes(root.right, max(mx, root.val))
        return left + right + (mx <= root.val)

