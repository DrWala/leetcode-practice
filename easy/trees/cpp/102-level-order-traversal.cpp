#include "../../../stdc++.h"
using std::queue;
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
    vector<vector<int>> levelOrder(TreeNode *root)
    {
        if (!root)
        {
            return {};
        }
        vector<vector<int>> ans;
        queue<TreeNode *> q;

        q.push(root);

        while (!q.empty())
        {
            vector<int> row;

            int size = q.size();
            while (size > 0)
            {
                TreeNode *node = q.front();
                q.pop();

                row.push_back(node->val);
                if (node->left != nullptr)
                {
                    q.push(node->left);
                }
                if (node->right != nullptr)
                {
                    q.push(node->right);
                }
                size--;
            }
            ans.push_back(row);
        }
        return ans;
    }
};
