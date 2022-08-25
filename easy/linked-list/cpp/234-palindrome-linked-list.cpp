
#include "../../../stdc++.h"
using std::vector;

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
    bool isPalindrome(ListNode *head)
    {
        vector<int> vect;
        while (head != nullptr)
        {
            vect.push_back(head->val);
            head = head->next;
        }

        for (size_t i = 0; i < vect.size() / 2; i++)
        {
            int back = vect.size() - i - 1;
            if (vect[i] != vect[back])
            {
                return false;
            }
        }
        return true;
    }
};
