#include <iostream>
#include <vector>
// using std::vector;
using namespace std;

class Solution
{
public:
    int removeDuplicates(vector<int> &nums)
    {
        int curr_idx = 0;
        int next_idx = 1;
        while (next_idx < nums.size())
        {
            if (nums[curr_idx] != nums[next_idx])
            {
                nums[curr_idx + 1] = nums[next_idx];
                curr_idx++;
            }
            next_idx++;
        }
        return curr_idx + 1;
    }
};

int main()
{
    Solution a;
    vector<int> vect{1, 1, 2};
    a.removeDuplicates(vect);
    for (int i : vect)
    {
        cout << i << ",";
    }
    cout << endl;
}
