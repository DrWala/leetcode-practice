#include "../../../stdc++.h"

using std::string;
using std::unordered_map;
using std::vector;
class Solution
{
public:
    vector<vector<string>> groupAnagrams(vector<string> &strs)
    {
        unordered_map<string, vector<string>> map;
        for (string s : strs)
        {
            string copy = s;
            std::sort(copy.begin(), copy.end());
            if (map.find(copy) == map.end())
            {
                map[copy] = vector<string>();
            }
            map[copy].push_back(s);
        }
        vector<vector<string>> res;
        for (auto &&kv : map)
        {
            res.push_back(kv.second);
        }

        return res;

        // Alternative:
        // unordered_map<string, vector<int>> map;
        // for (size_t i = 0; i < strs.size(); i++)
        // {
        //     string s = strs[i];
        //     std::sort(s.begin(), s.end());
        //     if (map.find(s) == map.end())
        //     {
        //         map[s] = vector<int>();
        //     }
        //     map[s].push_back(i);
        // }
        // vector<vector<string>> res;
        // for (auto &&kv : map)
        // {
        //     vector<string> intermediate;
        //     for (int &i : kv.second)
        //     {
        //         intermediate.push_back(strs[i]);
        //     }
        //     res.push_back(intermediate);
        // }

        // return res;
    }
};

void test(vector<string> strs)
{
    Solution a;
    vector<vector<string>> res = a.groupAnagrams(strs);
    for (auto &&v : res)
    {
        for (auto &&i : v)
        {
            std::cout << i << " ";
        }
        std::cout << std::endl;
    }
    std::cout << std::endl;
}

int main()
{
    Solution a;
    vector<string> v;
    v = {"eat", "tea", "tan", "ate", "nat", "bat"};
    test(v);
}
