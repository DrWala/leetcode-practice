#include "../../../stdc++.h"

using std::vector;

class Solution
{
public:
    void merge(vector<int> &nums1, int m, vector<int> &nums2, int n)
    {
        int i = m - 1, j = n - 1, tail = m + n - 1;
        while (i >= 0 && j >= 0)
        {
            if (nums1[i] > nums2[j] && i >= 0)
            {
                nums1[tail] = nums1[i];
                i--;
            }
            else if (j >= 0)
            {
                nums1[tail] = nums2[j];
                j--;
            }
            tail--;
        }

        while (i >= 0)
        {
            nums1[tail] = nums1[i];
            tail--;
            i--;
        }

        while (j >= 0)
        {
            nums1[tail] = nums2[j];
            tail--;
            j--;
        }
    }
};

void test(vector<int> &n1, int m, vector<int> &n2, int n)
{
    Solution a;
    a.merge(n1, m, n2, n);
    for (const int &i : n1)
    {
        std::cout << i << ", ";
    }
    std::cout << std::endl;
}

int main()
{
    vector<int> n1;
    vector<int> n2;
    n1 = {4, 5, 6, 0, 0, 0};
    n2 = {1, 2, 3};
    test(n1, 3, n2, 3);

    n1 = {1, 2, 3, 0, 0, 0};
    n2 = {2, 5, 6};
    test(n1, 3, n2, 3);

    n1 = {1, 2, 3, 4, 5, 0, 0, 0};
    n2 = {2, 5, 6};
    test(n1, 5, n2, 3);

    n1 = {1, 2, 0, 0, 0, 0, 0, 0};
    n2 = {3, 4, 5, 6, 7, 8};
    test(n1, 2, n2, 6);

    n1 = {0};
    n2 = {2};
    test(n1, 0, n2, 1);
}
