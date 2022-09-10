#include "../../../stdc++.h"

using std::vector;

class Solution
{
public:
    int maxSubArray(vector<int> &nums)
    {
        int max_sum = INT_MIN;
        int curr_sum = 0;
        for (size_t i = 0; i < nums.size(); i++)
        {
            curr_sum += nums[i];

            if (curr_sum > max_sum)
            {
                max_sum = curr_sum;
            }

            if (curr_sum < 0)
            {
                curr_sum = 0;
            }
        }
        return max_sum;
    }
};

void test(vector<int> &n)
{
    Solution a;
    int sum = a.maxSubArray(n);
    std::cout << sum << std::endl;
}

int main()
{
    vector<int> v = {-2, 1, -3, 4, -1, 2, 1, -5, 4};
    test(v);
}
