//
// Created by linkinpark213 on 5/14/19.
//
#include <iostream>

using namespace std;

struct TreeNode {
    int val;
    TreeNode *left;
    TreeNode *right;

    TreeNode(int x) : val(x), left(NULL), right(NULL) {}
};

class Solution {
public:
    bool isUnivalTree(TreeNode *root) {
        int value = root->val;
        bool unival = true;
        if (root->left != NULL) {
            if (root->left->val != value) return false;
            else unival = unival && isUnivalTree(root->left);
        }
        if (root->right != NULL) {
            if (root->right->val != value) return false;
            else unival = unival && isUnivalTree(root->right);
        }
        return unival;
    }
};

int main() {
    Solution solution;
    TreeNode root(2);
    root.left = new TreeNode(2);
    root.right = new TreeNode(2);
    root.left->left = new TreeNode(2);
    root.left->right = new TreeNode(2);
    cout << solution.isUnivalTree(&root);
}