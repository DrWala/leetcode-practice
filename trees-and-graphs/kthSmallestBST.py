# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def kthSmallest(self, root: TreeNode, k: int) -> int:
        return self.helper(root, k)[0]

    def helper(self, root: TreeNode, k: int):
        if root == None:
            return (None, k)
        else:
            left, l_rank = self.helper(root.left, k)

            l_rank -= 1

            if left != None:
                return (left, l_rank)

            if l_rank == 0:
                return (root.val, 0)

            return self.helper(root.right, l_rank)
