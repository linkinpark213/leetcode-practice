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
    vector<vector<int>> levelOrder(TreeNode* root) {
        vector<vector<int>> levels;
        if (root == NULL) return levels;
        queue<TreeNode*> nodeQueues[2];
        nodeQueues[0].push(root);
        int level = 0;
        while (!nodeQueues[level].empty()) {
            vector<int> numsInLevel;
            level = 1 - level;
            while (!nodeQueues[1 - level].empty()) {
                TreeNode* node = nodeQueues[1 - level].front();
                nodeQueues[1 - level].pop();
                numsInLevel.push_back(node->val);
                if (node->left != NULL) nodeQueues[level].push(node->left);
                if (node->right != NULL) nodeQueues[level].push(node->right);
            }
            levels.push_back(numsInLevel);
        }
        return levels;
    }
};

int main() {
    Solution solution;
    TreeNode* root = new TreeNode(3);
    root->left = new TreeNode(9);
    root->right = new TreeNode(20);
    root->right->left = new TreeNode(15);
    root->right->right = new TreeNode(7);
    auto ans = solution.levelOrder(root);
    for (auto it = ans.begin(); it != ans.end(); it++) {
        for (auto it2 = (*it).begin(); it2 != (*it).end(); it2++)
            cout << *it2 << " ";
        cout << endl;
    }
    return 0;
}