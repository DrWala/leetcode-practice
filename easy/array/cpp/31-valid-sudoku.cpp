#include "../../../stdc++.h"

using std::pair;
using std::unordered_set;
using std::vector;

class Solution
{
public:
    bool isValidSudoku(vector<vector<char>> &board)
    {
        // Row/col wise check
        for (int i = 0; i < 9; i++)
        {
            unordered_set<char> row_set;
            for (int j = 0; j < 9; j++)
            {
                char row_cell = board[i][j];
                if (row_cell == '.')
                    continue;

                if (row_set.find(row_cell) == row_set.end())
                {
                    row_set.insert(row_cell);
                }
                else
                {
                    return false;
                }
            }
        }
        for (int i = 0; i < 9; i++)
        {
            unordered_set<char> col_set;
            for (int j = 0; j < 9; j++)
            {
                char col_cell = board[j][i];
                if (col_cell == '.')
                    continue;

                if (col_set.find(col_cell) == col_set.end())
                {
                    col_set.insert(col_cell);
                }
                else
                {
                    return false;
                }
            }
        }
        vector<pair<int, int>> ranges = {std::make_pair(0, 3), std::make_pair(3, 6), std::make_pair(6, 9)};
        for (pair<int, int> r1 : ranges)
        {
            for (pair<int, int> r2 : ranges)
            {
                unordered_set<char> box_set;
                for (int i = r1.first; i < r1.second; i++)
                {
                    for (int j = r2.first; j < r2.second; j++)
                    {
                        char cell = board[i][j];
                        if (cell == '.')
                        {
                            continue;
                        }
                        else if (box_set.find(cell) == box_set.end())
                        {
                            box_set.insert(cell);
                        }
                        else
                        {
                            return false;
                        }
                    }
                }
            }
        }
        return true;
    }
};
int main()
{
    Solution a;
    vector<vector<char>> vect{
        {'5', '3', '.', '.', '7', '.', '.', '.', '.'},
        {'6', '.', '.', '1', '9', '5', '.', '.', '.'},
        {'.', '9', '8', '.', '.', '.', '.', '6', '.'},
        {'8', '.', '.', '.', '6', '.', '.', '.', '3'},
        {'4', '.', '.', '8', '.', '3', '.', '.', '1'},
        {'7', '.', '.', '.', '2', '.', '.', '.', '6'},
        {'.', '6', '.', '.', '.', '.', '2', '8', '.'},
        {'.', '.', '.', '4', '1', '9', '.', '.', '5'},
        {'.', '.', '.', '.', '8', '.', '.', '7', '9'}};
    bool valid = a.isValidSudoku(vect);
    std::cout << valid << std::endl;
}
