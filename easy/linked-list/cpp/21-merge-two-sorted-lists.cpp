#include "../../../stdc++.h"

struct ListNode
{
    int val;
    ListNode *next;
    ListNode() : val(0), next(nullptr) {}
    ListNode(int x) : val(x), next(nullptr) {}
    ListNode(int x, ListNode *next) : val(x), next(next) {}
};

class Solution
{
public:
    ListNode *mergeTwoLists(ListNode *list1, ListNode *list2)
    {
        ListNode *head = new ListNode(0);
        ListNode *ref = head;
        while (list1 != nullptr && list2 != nullptr)
        {
            if (list1->val < list2->val)
            {
                head->next = list1;
                list1 = list1->next;
            }
            else
            {
                head->next = list2;
                list2 = list2->next;
            }
            head = head->next;
        }
        if (list1 == nullptr)
        {
            head->next = list2;
        }
        else
        {
            head->next = list1;
        }
        return ref->next;
    }
};

void print(ListNode *head)
{
    while (head != nullptr)
    {
        std::cout << head->val << std::endl;
        head = head->next;
    }
}

int main()
{
    ListNode *ptr = new ListNode(1, new ListNode(3, new ListNode(5)));
    ListNode *ptr2 = new ListNode(2, new ListNode(4, new ListNode(6)));
    Solution a;
    ListNode *ref = a.mergeTwoLists(ptr, ptr2);
    print(ref);
}
