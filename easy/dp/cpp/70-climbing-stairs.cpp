#include "../../../stdc++.h"
using std::unordered_map;

class Solution
{
private:
    unordered_map<int, int> memo;

public:
    int climbStairs(int n)
    {
        for (int i = 0; i <= n; i++)
        {
            memo[i] = -1;
        }
        memo[0] = 0;
        memo[1] = 1;
        memo[2] = 2;

        return helper(n);
    }

    int helper(int n)
    {
        if (memo[n] != -1)
        {
            return memo[n];
        }
        else
        {
            memo[n] = helper(n - 1) + helper(n - 2);
        }
        return memo[n];
    }
};

void test(int n)
{
    Solution a;
    int result = a.climbStairs(n);
    std::cout << result << std::endl;
}

int main()
{
    // test(1);
    test(2);
    test(3);
    test(4);
}
