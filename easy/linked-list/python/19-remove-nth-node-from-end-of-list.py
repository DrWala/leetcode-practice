from typing import List, Optional
from collections import defaultdict
# Definition for singly-linked list.


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def __str__(self) -> str:
        f = ""
        x = self
        while x is not None:
            f += f"{x.val}->"
            x = x.next
        return f


class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        if head is None:
            return None
        nodes = {}
        ctr = 0
        while head is not None:
            nodes[ctr] = head
            head = head.next
            ctr += 1

        if n > ctr:
            return nodes[0]

        if n == ctr:
            return nodes[0].next

        # If we are deleting the last node, n + 1 node will not exist
        if n == 1:
            nodes[ctr - n - 1].next = None
            return nodes[0]

        nodes[ctr - n].val = nodes[ctr - n + 1].val
        nodes[ctr - n].next = nodes[ctr - n + 1].next
        return nodes[0]


# Regular remove
l = ListNode(1, ListNode(2, ListNode(3, ListNode(4, (ListNode(5))))))
print(Solution().removeNthFromEnd(l, 2))

# Remove only 1 item
l = ListNode(1)
print(Solution().removeNthFromEnd(l, 1))

# Empty list
l = None
print(Solution().removeNthFromEnd(l, 1))

# Remove last item
l = ListNode(1, ListNode(2))
print(Solution().removeNthFromEnd(l, 1))

# Remove first item
l = ListNode(1, ListNode(2, ListNode(3)))
print(Solution().removeNthFromEnd(l, 3))
