from typing import Optional
import math


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        return self.is_valid_bst_helper(root, -math.inf, math.inf)

    def is_valid_bst_helper(self, root: Optional[TreeNode], lower, upper):
        if not root:
            return True

        if lower < root.val < upper:
            return self.is_valid_bst_helper(root.left, lower, root.val) and self.is_valid_bst_helper(root.right, root.val, upper)
        else:
            return False
