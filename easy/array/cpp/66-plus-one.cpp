#include <iostream>
#include <vector>

using std::vector;

class Solution
{
public:
    vector<int> plusOne(vector<int> &digits)
    {
        int ptr = digits.size() - 1;
        while (ptr >= 0)
        {
            if (digits[ptr] != 9)
            {
                digits[ptr] += 1;
                return digits;
            }
            else
            {
                digits[ptr] = 0;
                ptr--;
            }
        }
        // This is the case where the number is like 99, we need to add a digit.
        // We set the first digit to 1 and add a 0 to the back, instead of prepending a 1
        digits[0] = 1;
        digits.push_back(0);
    }
};
