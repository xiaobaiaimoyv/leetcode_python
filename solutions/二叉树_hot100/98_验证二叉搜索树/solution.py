# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def check(self, root, left, right):
        if root is None:
            return True
        x = root.val
        return left < x < right and self.check(root.left, left, x) and self.check(root.right, x, right)

    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        return self.check(root, -inf, inf)

