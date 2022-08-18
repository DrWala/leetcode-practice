#include "../../../stdc++.h"

using std::vector;
class Solution
{
public:
    void reverseString(vector<char> &s)
    {
        for (int i = 0; i < s.size() / 2; i++)
        {
            int back = s.size() - i - 1;
            char temp = s[i];
            s[i] = s[back];
            s[back] = temp;
        }
    }
};
