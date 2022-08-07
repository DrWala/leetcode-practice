from typing import List, Optional


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
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        vals = []
        while head is not None:
            vals.append(head.val)
            head = head.next
        return vals == list(reversed(vals))


print(Solution().isPalindrome(ListNode(1, ListNode(2, ListNode(3)))))
print(Solution().isPalindrome(ListNode(1, ListNode(2, ListNode(1)))))
print(Solution().isPalindrome(ListNode(1)))
print(Solution().isPalindrome(None))
