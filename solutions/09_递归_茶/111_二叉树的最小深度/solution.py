# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0 
        l_d = self.minDepth(root.left)
        r_d = self.minDepth(root.right)
        if l_d == 0 or r_d == 0:
            ans = max(l_d, r_d) + 1
        else:
            ans = min(l_d , r_d ) + 1
        return ans
        