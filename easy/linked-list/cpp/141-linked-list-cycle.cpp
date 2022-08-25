
#include "../../../stdc++.h"
using std::unordered_set;

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
    bool hasCycle(ListNode *head)
    {
        // unordered_set<ListNode *> nodes;
        // while (head != nullptr)
        // {
        //     std::pair<std::unordered_set<ListNode *>::iterator, bool> ret = nodes.insert(head);
        //     if (ret.second == false)
        //     {
        //         return true;
        //     }
        //     head = head->next;
        // }
        // return false;
        ListNode *fast = head;
        ListNode *slow = head;
        while (fast != nullptr && fast->next != nullptr)
        {
            slow = slow->next;
            fast = fast->next->next;
            if (fast == slow)
            {
                return true;
            }
        }
        return false;
    }
};
