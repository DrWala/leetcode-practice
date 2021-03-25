
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next


"""
Approach:

Get each level of the binary tree and add them into an array
Then go through each item in the array and link one item to the next

How to deal with the binary tree as levels?

First, add the root's 2 children into an array. That is your "next level"
Then go through each item in "next level" and add each of their children into
another array. Keep going.
"""


class Solution:
    def connect(self, root: 'Node') -> 'Node':
        if root == None or root.left == None:
            return root

        cur_level = []
        next_level = []

        cur_level.append(root)
        root.next = None
        while True:
            item = cur_level[0]
            if item.left == None:
                break

            next_level.extend([item.left, item.right])

            del cur_level[0]

            if len(cur_level) == 0:
                for i, node in enumerate(next_level):
                    if i == len(next_level) - 1:
                        node.next = None
                    else:
                        node.next = next_level[i + 1]

                cur_level, next_level = next_level, cur_level
        return root


root = Node(1)
root.left = Node(2, Node(4), Node(5))
root.right = Node(3, Node(6), Node(7))
Solution().connect(Node())
