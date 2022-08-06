from typing import Optional
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
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # O(N) extra memory, O(N) time
        if head is None:
            return None

        nodes = {}
        ctr = -1
        while head is not None:
            ctr += 1
            nodes[ctr] = head
            head = head.next

        head = nodes[ctr]
        while ctr > 0:
            nodes[ctr].next = nodes[ctr - 1]
            ctr -= 1

        nodes[0].next = None

        return head

        # In place, O(N) time
        next, prev = None, None
        cur = head
        while cur is not None:
            next = cur.next
            cur.next = prev
            prev = cur
            cur = next
        return prev


print(Solution().reverseList(ListNode(1, ListNode(2, ListNode(3)))))
print(Solution().reverseList(ListNode(1)))
print(Solution().reverseList(None))
