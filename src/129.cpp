#include <iostream>

using namespace std;

/**
 * Definition for a binary tree node.
**/
struct TreeNode {
    int val;
    TreeNode *left;
    TreeNode *right;
    TreeNode(int x) : val(x), left(NULL), right(NULL) {}
};
 
class Solution {
    int sumNumbersRecursive(TreeNode* node, int curr) {
        if (node->left == NULL && node->right == NULL) return curr * 10 + node->val;
        int sum = 0;
        if (node->left != NULL) sum += sumNumbersRecursive(node->left, curr * 10 + node->val);
        if (node->right != NULL) sum += sumNumbersRecursive(node->right, curr * 10 + node->val);
        return sum;
    }
public:
    int sumNumbers(TreeNode* root) {
        if (root == NULL) return 0;
        return sumNumbersRecursive(root, 0);
    }
};

int main() {
    Solution solution;
    TreeNode *root = new TreeNode(4);
    root->left = new TreeNode(9);
    root->right = new TreeNode(0);
    root->left->left = new TreeNode(5);
    root->left->right = new TreeNode(1);
    cout << solution.sumNumbers(root);
}