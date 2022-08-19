#include "../../../stdc++.h"

using std::string;
using std::vector;
class Solution
{
public:
    bool isPalindrome(string s)
    {
        vector<char> new_str;
        for (char c : s)
        {
            if (isalnum(c))
            {
                c = tolower(c);
                new_str.push_back(c);
            }
        }
        for (size_t i = 0; i < new_str.size() / 2; i++)
        {
            int back = new_str.size() - i - 1;
            if (new_str[i] != new_str[back])
            {
                return false;
            }
        }
        return true;
    }
};

int main()
{
    string s = "A man, a plan, a canal: Panama";
    Solution a;
    bool result = a.isPalindrome(s);
    std::cout << result << std::endl;
}
