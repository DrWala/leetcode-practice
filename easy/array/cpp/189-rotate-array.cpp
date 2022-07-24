#include <iostream>
#include <vector>

using std::vector;

template <class X>
void print_vector(vector<X> vect)
{
    for (X i : vect)
    {
        std::cout << i << " ";
    }
    std::cout << std::endl;
}

class Solution
{
public:
    void rotate(vector<int> &nums, int k)
    {
        int n = nums.size();
        if (k > n)
        {
            k = k % n;
        }
        vector<int>
            temp(n);

        for (size_t i = 0; i < n - k; i++)
        {
            temp[i + k] = nums[i];
        }

        for (size_t i = 0; i < k; i++)
        {
            temp[i] = nums[n - k + i];
        }

        for (size_t i = 0; i < nums.size(); i++)
        {
            nums[i] = temp[i];
        }
    }
};

int main()
{
    Solution a;
    vector<int> vect{1, 2, 3, 4, 5, 6, 7};
    a.rotate(vect, 7);
    print_vector(vect);
}
