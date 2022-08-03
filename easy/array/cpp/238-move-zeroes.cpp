#include <iostream>
#include <vector>
#include <algorithm>

using std::vector;

class Solution
{
public:
    void moveZeroes(vector<int> &nums)
    {
        int slow = 0;
        for (size_t i = 0; i < nums.size(); i++)
        {
            int prev = nums[slow];
            int curr = nums[i];

            if (prev != 0)
            {
                slow += 1;
                continue;
            }

            if (curr != 0 && prev == 0)
            {
                std::iter_swap(nums.begin() + slow, nums.begin() + i);
                slow += 1;
            }
        }
    }
};
