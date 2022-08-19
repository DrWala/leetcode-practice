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
    ListNode *reverseList(ListNode *head)
    {
        ListNode *prev = nullptr;
        ListNode *next = nullptr;
        ListNode *curr = head;
        while (curr != nullptr)
        {
            next = curr->next;
            curr->next = prev;
            prev = curr;
            curr = next;
        }
        return prev;
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
    Solution a;
    ListNode *ptr, *res;
    ptr = new ListNode(0, new ListNode(1, new ListNode(2, new ListNode(3, new ListNode(4)))));
    res = a.reverseList(ptr);
    print(res);
}
