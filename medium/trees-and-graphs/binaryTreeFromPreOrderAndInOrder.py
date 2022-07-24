# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


"""
Approach:
The first item in the pre order traversal tells you where the root is.
Using that root as the marker, split the inorder traversal into left and right

Now that you have left and right, your pre order array can be visualised as such:
[[root][items on left of root][items on right of root]]

You may not know where the boundaries of the left and right in preorder are, 
but you know how many elements there are there from your left and right split of
the inorder traversal. Use that to break it up.

Now you can recursively solve this.
"""


class Solution:
    def buildTree(self, preorder, inorder):
        if len(inorder) == 0:
            return None
        elif len(inorder) == 1:
            return TreeNode(inorder[0])

        root = preorder[0]
        root_idx = inorder.index(root)
        left = inorder[:root_idx]
        right = inorder[root_idx + 1:]

        preorder_left = preorder[1: len(left) + 1]
        preorder_right = preorder[-len(right):]

        return TreeNode(root, self.buildTree(preorder_left, left), self.buildTree(preorder_right, right))


print(Solution().buildTree(
    [3, 9, 20, 15, 7],
    [9, 3, 15, 20, 7]))
