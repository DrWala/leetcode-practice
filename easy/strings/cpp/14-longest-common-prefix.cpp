#include "../../../stdc++.h"

using std::string;
using std::vector;

class Solution
{
public:
    string longestCommonPrefix(vector<string> &strs)
    {
        if (strs.size() == 0)
        {
            return "";
        }

        if (strs.size() == 1)
        {
            return strs[0];
        }

        int shortest_len = INT_MAX;
        for (const string &s : strs)
        {
            shortest_len = std::min((int)s.size(), shortest_len);
        }

        for (int j = 0; j < shortest_len; j++)
        {
            char first = strs[0][j];
            for (size_t i = 1; i < strs.size(); i++)
            {
                char first = strs[0][j];
                for (size_t i = 0; i < strs.size(); i++)
                {
                    if (strs[i][j] != first)
                    {
                        return std::string(strs[0].begin(), strs[0].begin() + j);
                    }
                }
            }
        }
        return string(strs[0].begin(), strs[0].begin() + shortest_len);
    }
};

int main()
{
    Solution a;
    vector<string> v;
    v = {"ab", "a"};
    std::cout << a.longestCommonPrefix(v) << std::endl;
    v = {"flower", "flow", "flight"};
    std::cout << a.longestCommonPrefix(v) << std::endl;
    v = {"flo", "flow", "flower", "flight"};
    std::cout << a.longestCommonPrefix(v) << std::endl;
    v = {"flo", "flow", "flower", "flooo"};
    std::cout << a.longestCommonPrefix(v) << std::endl;
    v = {"flower"};
    std::cout << a.longestCommonPrefix(v) << std::endl;
    v = {"a"};
    std::cout << a.longestCommonPrefix(v) << std::endl;
    v = {""};
    std::cout << a.longestCommonPrefix(v) << std::endl;
    v = {};
    std::cout << a.longestCommonPrefix(v) << std::endl;
}
