# Key learning: Don't do this:
# node = ListNode(x)
# tail.next = node
# When you overwrite node, the reference at tail.next will also break

# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        len_1 = self.getLength(l1)
        len_2 = self.getLength(l2)

        if len_1 > len_2:
            longer = l1
            shorter = l2
        else:
            shorter = l1
            longer = l2
        
        head = ListNode()
        tail = head
        carry = 0
        while longer is not None:
            onesum = longer.val + shorter.val + carry
            val = onesum - 10 if onesum >= 10 else onesum
            carry = 1 if onesum >= 10 else 0
            tail.next = ListNode(val)
            tail = tail.next

            longer = longer.next
            shorter = shorter.next if shorter.next is not None else ListNode(0)
        if carry == 1:
            tail.next = ListNode(1)
        return head.next

    def getLength(self, ll):
        i = 0
        while ll.next is not None:
            i += 1
            ll = ll.next
        return i

    def parse(self, arr):
        head = ListNode(arr[0])
        tail = head
        for i in arr[1:]:
            node = ListNode(i)
            tail.next = node
            tail = node
        return head
    
    def print(self, ll):
        arr = []
        while ll is not None:
            arr.append(ll.val)
            ll = ll.next
        print(arr)

l1 = [9, 9, 9, 9, 9, 9, 9]
l2 = [9, 9, 9, 9]
l1 = [0]
l2 = [0]
l1 = [2, 4, 3]
l2 = [5, 6, 4]

l1 = Solution().parse(l1)
l2 = Solution().parse(l2)

ans = Solution().addTwoNumbers(l1, l2)
Solution().print(ans)


