#include "../../../stdc++.h"

using std::unordered_set;
using std::vector;

class Solution
{
public:
    void setZeroes(vector<vector<int>> &matrix)
    {
        bool r0 = false, c0 = false;
        for (size_t i = 0; i < matrix.size(); i++)
        {
            for (size_t j = 0; j < matrix[0].size(); j++)
            {
                if (matrix[i][j] == 0)
                {
                    if (i == 0 && j == 0)
                    {
                        r0 = true;
                        c0 = true;
                        continue;
                    }
                    if (i == 0)
                    {
                        r0 = true;
                        continue;
                    }
                    if (j == 0)
                    {
                        c0 = true;
                        continue;
                    }
                    matrix[0][j] = 0;
                    matrix[i][0] = 0;
                }
            }
        }

        for (size_t i = 1; i < matrix.size(); i++)
        {
            if (matrix[i][0] == 0)
            {
                for (size_t j = 0; j < matrix[0].size(); j++)
                {
                    matrix[i][j] = 0;
                }
            }
        }
        for (size_t j = 1; j < matrix[0].size(); j++)
        {
            if (matrix[0][j] == 0)
            {
                for (size_t i = 0; i < matrix.size(); i++)
                {
                    matrix[i][j] = 0;
                }
            }
        }

        if (r0)
        {
            for (size_t j = 0; j < matrix[0].size(); j++)
            {
                matrix[0][j] = 0;
            }
        }
        if (c0)
        {
            for (size_t i = 0; i < matrix.size(); i++)
            {
                matrix[i][0] = 0;
            }
        }
    }
};

void test(vector<vector<int>> &nums)
{
    Solution a;
    a.setZeroes(nums);
    for (auto &&v : nums)
    {
        for (auto &&i : v)
        {
            std::cout << i << " ";
        }
        std::cout << std::endl;
    }
    std::cout << std::endl;
}

int main()
{
    vector<vector<int>> v;
    v = {{0, 1, 2, 0},
         {3, 4, 5, 2},
         {1, 3, 1, 5}};
    test(v);
    v = {
        {0, 5, 6, 6, 9},
        {7, 0, 3, 3, 1},
        {1, -2147483648, 7, 2147483647, 8}};

    test(v);
    v = {{1, 2, 3, 4},
         {5, 0, 7, 8},
         {0, 10, 11, 12},
         {13, 14, 15, 0}};
    test(v);
}
