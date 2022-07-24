#include <iostream>
#include <vector>
using namespace std;

class Solution
{
public:
    int maxProfit(vector<int> &prices)
    {
        int buy = 0;
        int sell = 0;
        int profit = 0;
        while (sell < prices.size())
        {
            int curr_profit = prices[sell] - prices[buy];
            if (curr_profit > 0)
            {
                profit += curr_profit;
            }
            buy = sell;
            sell = sell + 1;
        }
        return profit;
    }
};

int main()
{
    Solution a;
    vector<int> vect{7, 1, 5, 3, 6, 4};
    int profit = a.maxProfit(vect);
    cout << profit << endl;
}
