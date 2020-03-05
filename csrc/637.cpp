#include <iostream>
#include <vector>
#include <queue>

using namespace std;

// Definition for a binary tree node.
struct TreeNode {
    int val;
    TreeNode *left;
    TreeNode *right;
    TreeNode(int x) : val(x), left(NULL), right(NULL) {}
};


class Solution {
public:
    vector<double> averageOfLevels(TreeNode* root) {
        vector<double> averages;
        if (root == NULL) return averages;
        queue<TreeNode*> nodeQueues[2];
        nodeQueues[0].push(root);
        int level = 0, count = 0;
        double sum = 0.0;
        while (!nodeQueues[level].empty()) {
            vector<int> numsInLevel;
            level = 1 - level;
            sum = 0.0;
            count = 0;
            while (!nodeQueues[1 - level].empty()) {
                TreeNode* node = nodeQueues[1 - level].front();
                nodeQueues[1 - level].pop();
                sum += node->val;
                count++;
                if (node->left != NULL) nodeQueues[level].push(node->left);
                if (node->right != NULL) nodeQueues[level].push(node->right);
            }
            averages.push_back(sum / count);
        }
        return averages;
    }
};

int main() {
    Solution solution;
    TreeNode* root = new TreeNode(3);
    root->left = new TreeNode(9);
    root->right = new TreeNode(20);
    root->right->left = new TreeNode(15);
    root->right->right = new TreeNode(7);
    vector<double> ans = solution.averageOfLevels(root);
    for (auto it = ans.begin(); it != ans.end(); it++)
        cout << *it << " ";
    return 0;
}