class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution(object):
    def getIntersectionNode(self, headA, headB):
        """
        :type head1, head1: ListNode
        :rtype: ListNode
        """
        first_list = set()
        while headA is not None:
            first_list.add(headA)
            headA = headA.next
        
        while headB is not None:
            if headB in first_list:
                return headB
            else:
                headB = headB.next
        return None