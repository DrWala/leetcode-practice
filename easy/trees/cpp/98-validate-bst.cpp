#include "../../../stdc++.h"
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
    bool isValidBST(TreeNode *root)
    {
        return bst_helper(root, LONG_MIN, LONG_MAX);
    }
    bool bst_helper(TreeNode *node, long lower, long upper)
    {
        if (node == nullptr)
        {
            return true;
        }
        if (lower < node->val && node->val < upper)
        {
            return bst_helper(node->left, lower, node->val) && bst_helper(node->right, node->val, upper);
        }
        return false;
    }
};
