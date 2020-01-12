#include <iostream>
#include <vector>
#include <stack>

using namespace std;

struct TreeNode {
    int val;
    TreeNode *left;
    TreeNode *right;
    TreeNode(int x) : val(x), left(NULL), right(NULL) {}
};

class Solution {
public:
    vector<int> preorderTraversal(TreeNode* root) {
        vector<int> reordered;
        if (root == NULL) return reordered;
        stack<TreeNode*> nodeStack;
        nodeStack.push(root);
        while (!nodeStack.empty()) {
            TreeNode* node = nodeStack.top();
            nodeStack.pop();
            reordered.push_back(node->val);
            if (node->right != NULL) nodeStack.push(node->right);
            if (node->left != NULL) nodeStack.push(node->left);
        }
        return reordered;
    }
};

int main() {
    Solution solution;
    TreeNode* root = new TreeNode(1);
    root->right = new TreeNode(2);
    root->right->left = new TreeNode(3);
    auto ans = solution.preorderTraversal(root);
    for (auto it = ans.begin(); it != ans.end(); it++) {
        cout << *it << " ";
    }
    return 0;
}