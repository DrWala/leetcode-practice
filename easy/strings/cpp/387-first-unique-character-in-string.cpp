#include "../../../stdc++.h"

using std::string;
using std::unordered_map;
using std::vector;
class Solution
{
public:
    int firstUniqChar(string s)
    {
        unordered_map<char, vector<int>> map;
        for (size_t i = 0; i < s.length(); i++)
        {
            map[s[i]].push_back(i);
        }
        int lowest = INT_MAX;
        for (auto &it : map)
        {
            if (it.second.size() == 1)
            {
                lowest = std::min(lowest, it.second[0]);
            }
        }
        return lowest == INT_MAX ? -1 : lowest;
    }
};

int main()
{
    string s = "aabb";
    Solution a;
    int output = a.firstUniqChar(s);
    std::cout << output << std::endl;
}
