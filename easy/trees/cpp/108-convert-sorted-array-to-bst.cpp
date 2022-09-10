#include "../../../stdc++.h"

using std::vector;

struct TreeNode
{
    int val;
    TreeNode *left;
    TreeNode *right;
    TreeNode() : val(0), left(nullptr), right(nullptr) {}
    TreeNode(int x) : val(x), left(nullptr), right(nullptr) {}
    TreeNode(int x, TreeNode *left, TreeNode *right) : val(x), left(left), right(right) {}
};

class Solution
{
public:
    TreeNode *sortedArrayToBST(vector<int> &nums)
    {
        return helper(nums, 0, nums.size());
    }

    TreeNode *helper(vector<int> &nums, int left, int right)
    {
        if (left == right)
        {
            return nullptr;
        }

        int center = (right + left) / 2;
        TreeNode *node = new TreeNode(nums[center]);

        node->left = helper(nums, left, center);
        node->right = helper(nums, center + 1, right);
        return node;
    }
};
