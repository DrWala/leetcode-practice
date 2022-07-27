#include <iostream>
#include <vector>
#include <unordered_map>

using std::unordered_map;
using std::vector;

class Solution
{
public:
    vector<int> intersect(vector<int> &nums1, vector<int> &nums2)
    {
        if (nums1.size() > nums2.size())
        {
            return intersect(nums2, nums1);
        }

        unordered_map<int, int> counter;
        for (int n : nums1)
        {
            counter[n]++;
        }

        vector<int> ans;

        for (int n : nums2)
        {
            if (counter[n] > 0)
            {
                ans.push_back(n);
                counter[n]--;
            }
        }
        return ans;
    }
};

// Follow up questions:
// Q: What if the given array is already sorted? How would you optimize your algorithm?
// A: No change
// Q: What if nums1's size is small compared to nums2's size? Which algorithm is better?
// A: Smaller one goes into the map, bigger one you iterate through. Less extra space needed
// Q: What if elements of nums2 are stored on disk, and the memory is limited such that you cannot load all elements into the memory at once?
// A: Smaller one goes into the map, if both dont fit in memory then break into chunks and process
