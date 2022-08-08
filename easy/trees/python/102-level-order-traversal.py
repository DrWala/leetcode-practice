from typing import Optional, List


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        q = []
        res = []
        if root:
            res.append([root.val])
            q.append(root)
        while q:
            children = []
            for node in q:
                left = node.left
                right = node.right

                if left:
                    children.append(left)
                if right:
                    children.append(right)
            if children:
                res.append([child.val for child in children])
                q = children
            else:
                break

        return res
