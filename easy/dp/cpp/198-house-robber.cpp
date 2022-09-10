#include "../../../stdc++.h"

using std::unordered_map;
using std::vector;
class Solution
{
private:
    unordered_map<int, int> memo;

public:
    int rob(vector<int> &nums)
    {
        memo[0] = nums[0];
        for (size_t i = 1; i < nums.size(); i++)
        {
            memo[i] = -1;
        }

        return helper(nums, nums.size() - 1);
    }
    int helper(vector<int> &nums, int r)
    {

        if (r < 0)
        {
            return 0;
        }

        if (memo[r] != -1)
        {
            return memo[r];
        }

        memo[r] = std::max(
            helper(nums, r - 1),
            helper(nums, r - 2) + nums[r]);
        return memo[r];
    }
};

void test(vector<int> &n)
{
    Solution a;
    int sum = a.rob(n);
    std::cout << sum << std::endl;
}

int main()
{
    vector<int> v;
    v = {1, 2, 3, 1};
    test(v);
    v = {0};
    test(v);
}
