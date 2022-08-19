#include "../../../stdc++.h"

using std::string;
using std::vector;

class Solution
{
public:
    int myAtoi(string s)
    {
        int start = 0;
        bool sign = true;
        for (size_t i = 0; i < s.size(); i++)
        {
            if (s[i] != ' ')
            {
                start = i;
                if (s[i] == '-' || s[i] == '+')
                {
                    sign = s[i] == '+';
                    start = i + 1;
                }
                break;
            }
        }
        string::iterator it = s.begin() + start;
        long ans = 0;
        while (isdigit(*it) && it != s.end())
        {
            ans = ans * 10 + (*it - '0');
            if (ans > INT_MAX && sign)
            {
                return INT_MAX;
            }
            if (ans > INT_MAX && !sign)
            {
                return INT_MIN;
            }
            it++;
        }
        ans = sign ? ans : -1 * ans;

        return (int)ans;
    }
};

int main()
{
    Solution a;
    string s;
    s = "42";
    std::cout << a.myAtoi(s) << std::endl;
    s = "-91283472332";
    std::cout << a.myAtoi(s) << std::endl;
    s = "20000000000000000000";
    std::cout << a.myAtoi(s) << std::endl;
    s = "+4193";
    std::cout << a.myAtoi(s) << std::endl;
    s = "41";
    std::cout << a.myAtoi(s) << std::endl;
    s = "          -42";
    std::cout << a.myAtoi(s) << std::endl;
    s = "43 with many words";
    std::cout << a.myAtoi(s) << std::endl;
    s = "many words but i see 0";
    std::cout << a.myAtoi(s) << std::endl;
    s = "4193";
    std::cout << a.myAtoi(s) << std::endl;
}
