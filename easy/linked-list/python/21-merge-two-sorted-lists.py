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
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        new_list = ListNode(-1)
        copy = new_list
        while list1 is not None and list2 is not None:
            l1 = list1.val
            l2 = list2.val

            if l1 < l2:
                new_list.next = list1
                list1 = list1.next
            else:
                new_list.next = list2
                list2 = list2.next
            new_list = new_list.next
            new_list.next = None

        if list1 is None:
            new_list.next = list2
        elif list2 is None:
            new_list.next = list1

        return copy.next


print(Solution().mergeTwoLists(ListNode(1, ListNode(2,
      ListNode(3))), ListNode(4, ListNode(5, ListNode(6)))))

print(Solution().mergeTwoLists(ListNode(1, ListNode(3,
      ListNode(5))), ListNode(2, ListNode(4, ListNode(6)))))

print(Solution().mergeTwoLists(ListNode(1, ListNode(3, ListNode(5))), ListNode(6)))

print(Solution().mergeTwoLists(ListNode(1), ListNode(2, ListNode(4, ListNode(6)))))

print(Solution().mergeTwoLists(None, ListNode(4, ListNode(5, ListNode(6)))))

print(Solution().mergeTwoLists(ListNode(1, ListNode(2, ListNode(3))), None))
