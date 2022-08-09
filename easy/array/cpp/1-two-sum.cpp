#include "../../../stdc++.h"

using std::unordered_map;
using std::vector;

class Solution
{
public:
    vector<int> twoSum(vector<int> &nums, int target)
    {
        unordered_map<int, int> map;
        for (int i = 0; i < nums.size(); i++)
        {
            int value = nums[i];
            if (map.find(target - value) != map.end())
            {
                int otherindex = map.find(target - value)->second;
                return {i, otherindex};
            }
            else
            {
                map[value] = i;
            }
        }
        return {};
    }
};

int main()
{
    Solution a;
    vector<int> vect = {1, 2, 3, 4};
    a.twoSum(vect, 5);
}
