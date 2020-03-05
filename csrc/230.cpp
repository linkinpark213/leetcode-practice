#include <iostream>

using namespace std;

struct TreeNode {
    int val;
    TreeNode *left;
    TreeNode *right;
    TreeNode(int x) : val(x), left(NULL), right(NULL) {}
};

class Solution {
    int dfs(TreeNode* node, int &k) {
        if (node == NULL) return -1;
        int ans;
        ans = dfs(node->left, k);
        if (k == 0) return ans;
        k--;
        if (k == 0) return node->val;
        return dfs(node->right, k);
    }
public:
    int kthSmallest(TreeNode* root, int k) {
        return dfs(root, k);
    }
};

int main() {
    Solution solution;
    TreeNode* root = new TreeNode(5);
    root->left = new TreeNode(3);
    root->right = new TreeNode(6);
    root->left->left = new TreeNode(2);
    root->left->right = new TreeNode(4);
    root->left->left->left = new TreeNode(1);
    cout << solution.kthSmallest(root, 3);
    return 0;
}