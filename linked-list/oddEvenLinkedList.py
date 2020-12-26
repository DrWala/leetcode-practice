# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution(object):
    def oddEvenList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if head is None:
            return None
        odd = head
        even = head.next
        even_store = head.next
        while odd is not None and even is not None and odd.next is not None and even.next is not None:
            odd.next = odd.next.next
            even.next = even.next.next
            odd = odd.next
            even = even.next
        odd.next = even_store
        return head

    
    def parse(self, arr):
        head = ListNode()
        tail = head
        for i in arr:
            node = ListNode(i)
            tail.next = node
            tail = node
        return head.next if head.next is not None else None
    
    def print(self, ll):
        arr = []
        while ll is not None:
            arr.append(ll.val)
            ll = ll.next
        print(arr)

l1 = [2, 1, 3, 5, 6, 4, 7]
l1 = [1, 2, 3, 4, 5]
l1 = [1, 2, 3, 4, 5, 6, 7, 8]
# l1 = []


l1 = Solution().parse(l1)
ans = Solution().oddEvenList(l1)
Solution().print(ans)