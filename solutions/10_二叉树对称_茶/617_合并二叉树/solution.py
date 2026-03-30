class Solution:
    def mergeTrees(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> Optional[TreeNode]:
        # 1. 基准条件：如果一方为空，直接返回另一方（包含了两方都为空的情况）
        if not root1:
            return root2
        if not root2:
            return root1

        # 2. 合并当前节点的值
        # 走到这里说明 root1 和 root2 都不为空，直接相加即可
        root1.val += root2.val

        # 3. 关键：递归合并子树，并将合并后的结果“接”在 root1 上
        root1.left = self.mergeTrees(root1.left, root2.left)
        root1.right = self.mergeTrees(root1.right, root2.right)

        # 4. 返回合并后的当前节点
        return root1