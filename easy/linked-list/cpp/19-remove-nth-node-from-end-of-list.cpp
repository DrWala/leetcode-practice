struct ListNode
{
    int val;
    ListNode *next;
    ListNode() : val(0), next(nullptr) {}
    ListNode(int x) : val(x), next(nullptr) {}
    ListNode(int x, ListNode *next) : val(x), next(next) {}
};

#include "../../../stdc++.h"

using std::unordered_map;

class Solution
{
public:
    ListNode *removeNthFromEnd(ListNode *head, int n)
    {
        unordered_map<int, ListNode *> map;
        int counter = 0;
        while (head != nullptr)
        {
            map[counter] = head;
            head = head->next;
            counter++;
        }
        counter--;

        // Remove 1st item
        if (n == counter + 1)
        {
            return map[0]->next;
        }

        // Remove last item
        if (n == 0)
        {
            // There is only 1 item in the list
            if (counter == 0)
            {
                return nullptr;
            }

            // Make next item of second last item null
            map[counter - 1]->next = nullptr;
            return map[0];
        }

        map[counter - n]->next = map[counter - n + 2];
        return map[0];
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
    ListNode *ptr;
    // ListNode *ptr = new ListNode(1, new ListNode(2, new ListNode(3, new ListNode(4, new ListNode(5)))));
    // a.removeNthFromEnd(ptr, 3);
    // print(ptr);

    // std::cout << "==========" << std::endl;

    // ptr = new ListNode(1, new ListNode(2, new ListNode(3, new ListNode(4, new ListNode(5)))));
    // a.removeNthFromEnd(ptr, 2);
    // print(ptr);

    // std::cout << "==========" << std::endl;

    // ptr = new ListNode(10);
    // a.removeNthFromEnd(ptr, 1);

    // std::cout << "==========" << std::endl;

    ptr = new ListNode(1, new ListNode(2));
    ListNode *res = a.removeNthFromEnd(ptr, 2);
    print(res);
}
