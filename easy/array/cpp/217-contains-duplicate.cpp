#include <iostream>
#include <vector>
#include <unordered_set>

using std::unordered_set;
using std::vector;

class Solution
{
public:
    bool containsDuplicate(vector<int> &nums)
    {
        // Old approach, will throw everything into the set which is very slow
        // unordered_set<int> dupset(nums.begin(), nums.end());
        // return dupset.size() != nums.size();

        // New approach: terminate early when size of set does not match against no. of items
        unordered_set<int> dupset;
        for (size_t i = 0; i < nums.size(); i++)
        {
            dupset.insert(nums[i]);
            if (dupset.size() <= i)
            {
                return true;
            }

            // Alternative approach: insert returns a pair whose second param tells us if insertion took place.
            // auto p = dupset.insert(nums[i]);
            // if (!p.second)
            // {
            //     return true;
            // }
        }
        return false;
    }
};
int main()
{
    Solution a;
    vector<int> *vect = new vector<int>{1, 2, 3, 4};
    bool dup = a.containsDuplicate(*vect);
    std::cout << dup << std::endl;

    delete vect;
    vect = new vector<int>{1, 2, 3, 1};

    dup = a.containsDuplicate(*vect);
    std::cout << dup << std::endl;
}
