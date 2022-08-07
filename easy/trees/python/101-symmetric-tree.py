from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        return self.is_symmetric_helper(root.left, root.right)

    def is_symmetric_helper(self, left: Optional[TreeNode], right: Optional[TreeNode]):
        if left is None and right is None:
            return True
        if left is None or right is None:
            return False
        if left.val != right.val:
            return False
        return self.is_symmetric_helper(left.left, right.right) and self.is_symmetric_helper(left.right, right.left)
