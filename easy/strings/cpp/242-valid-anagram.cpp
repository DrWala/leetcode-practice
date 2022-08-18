#include "../../../stdc++.h"

using std::string;
using std::unordered_map;
class Solution
{
public:
    bool isAnagram(string s, string t)
    {
        unordered_map<char, int> map1;
        for (char c : s)
        {
            map1[c]++;
        }

        unordered_map<char, int> map2;
        for (char c : t)
        {
            map2[c]++;
        }
        return map1 == map2;
    }
};

int main()
{
    return 0;
}
