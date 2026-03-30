class Solution:
    def isUnivalTree(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True

        # 记录标准值（根节点的值）
        target = root.val

        def check(node):
            # 1. 基准条件：如果走到空节点，说明这条路径没问题
            if not node:
                return True

            # 2. 核心判断：当前节点值是否等于标准值
            if node.val != target:
                return False

            # 3. 递归：左子树和右子树都必须满足条件 (用 and 连接)
            return check(node.left) and check(node.right)

        return check(root)