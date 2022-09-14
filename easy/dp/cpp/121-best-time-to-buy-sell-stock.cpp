#include "../../../stdc++.h"

using std::vector;

class Solution
{
public:
    int maxProfit(vector<int> &prices)
    {
        int min_price = INT_MAX;
        int profit = 0;
        for (const int &i : prices)
        {
            min_price = std::min(i, min_price);
            profit = std::max(profit, i - min_price);
        }
    }
};
