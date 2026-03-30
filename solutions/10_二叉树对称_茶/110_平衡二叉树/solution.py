# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        def getheight(node):
            if node is None:
                return 0
            l_h = getheight(node.left)
            if l_h == -1:
                return -1
            r_h = getheight(node.right)
            if r_h == -1 or abs(l_h - r_h) > 1:
                return -1
            return max(l_h, r_h) + 1

        return getheight(root) != -1

