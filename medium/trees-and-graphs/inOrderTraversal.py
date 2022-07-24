class Solution(object):
    def inorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        arr = []
        def helper(root):
            if root is None:
                return None
            else:
                helper(root.left)
                arr.append(root.val)
                helper(root.right)
        helper(root)
        return arr