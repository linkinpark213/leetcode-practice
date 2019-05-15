//
// Created by linkinpark213 on 5/15/19.
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

    int sumRootToLeafWithPrev(TreeNode *root, int prev_sum, int &total_sum) {
        if (root->left != NULL) {
            sumRootToLeafWithPrev(root->left, prev_sum * 2 + root->val, total_sum);
        }
        if (root->right != NULL) {
            sumRootToLeafWithPrev(root->right, prev_sum * 2 + root->val, total_sum);
        }
        if (root->left == NULL && root->right == NULL) {
            total_sum += prev_sum * 2 + root->val;
        }
        return total_sum;
    }

public:
    int sumRootToLeaf(TreeNode *root) {
        int total_sum = 0;
        return sumRootToLeafWithPrev(root, 0, total_sum);
    }
};

int main() {
    Solution solution;
    TreeNode root(1);
    root.left = new TreeNode(0);
    root.left->left = new TreeNode(0);
    root.left->right = new TreeNode(1);
    root.right = new TreeNode(1);
    root.right->left = new TreeNode(0);
    root.right->right = new TreeNode(1);
    cout << solution.sumRootToLeaf(&root);
}