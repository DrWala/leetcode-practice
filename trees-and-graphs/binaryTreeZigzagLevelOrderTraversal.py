# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    def __str__(self):
        return self.val


class Solution:
    def zigzagLevelOrder(self, root: TreeNode):
        if root == None:
            return []
        else:
            final = [[root]]
            ltr = False
            cur_level = [root]
            next_level = []

            while (len(cur_level) > 0):
                idx = -1

                root = cur_level[idx]

                if ltr:
                    if root.left is not None:
                        next_level.append(root.left)

                    if root.right is not None:
                        next_level.append(root.right)
                else:
                    if root.right is not None:
                        next_level.append(root.right)

                    if root.left is not None:
                        next_level.append(root.left)

                del cur_level[idx]

                if len(cur_level) == 0:
                    if len(next_level) > 0:
                        final.append(next_level[:])
                    cur_level, next_level = next_level, cur_level
                    ltr = not ltr

        final = [list(map(lambda x: x.val, arr)) for arr in final]

        return final


root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.left = TreeNode(7)
root.left.right = TreeNode(6)
root.right.left = TreeNode(5)
root.right.right = TreeNode(4)

print(Solution().zigzagLevelOrder(root))
