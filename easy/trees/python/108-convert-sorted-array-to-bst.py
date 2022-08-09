from typing import List, Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    def __str__(self) -> str:
        return f"root: {self.val} left: {self.left}: right: {self.right}"


class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        return self.helper(nums, 0, len(nums))

    def helper(self, nums, left, right):
        print(f"left: {left}: right: {right}")
        if left == right:
            return None
        center = (right + left)//2
        root = TreeNode(nums[center])
        root.left = self.helper(nums, left, center)
        root.right = self.helper(nums, center + 1, right)
        return root


print(Solution().sortedArrayToBST([-10, -3, 0, 5, 9]))
