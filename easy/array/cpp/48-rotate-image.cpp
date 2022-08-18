#include "../../../stdc++.h"

using std::vector;

class Solution
{
public:
    void rotate(vector<vector<int>> &matrix)
    {
        for (int i = 0; i < matrix.size(); i++)
        {
            for (int j = 0; j < i; j++)
            {
                int temp = matrix[i][j];
                matrix[i][j] = matrix[j][i];
                matrix[j][i] = temp;
            }
        }
        for (int i = 0; i < matrix.size(); i++)
        {
            for (int j = 0; j < matrix[i].size() / 2; j++)
            {
                int other_idx = matrix[i].size() - j - 1;
                int temp = matrix[i][j];
                matrix[i][j] = matrix[i][other_idx];
                matrix[i][other_idx] = temp;
            }
        }
    }
};

int main()
{
    vector<vector<int>> vect = {{1, 2, 3}, {4, 5, 6}, {7, 8, 9}};
    Solution a;
    a.rotate(vect);
    return 0;
}
