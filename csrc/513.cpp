#include <iostream>
#include <queue>

using namespace std;

struct TreeNode {
    int val;
    TreeNode *left;
    TreeNode *right;
    TreeNode(int x) : val(x), left(NULL), right(NULL) {}
};

class Solution {
public:
    int findBottomLeftValue(TreeNode* root) {
        TreeNode* leftPtr;
        TreeNode* ptr;
        queue<TreeNode*> nodeQueues[2];
        int level = 0;
        nodeQueues[0].push(root);
        while (!nodeQueues[level].empty()) {
            leftPtr = nodeQueues[level].front();
            while(!nodeQueues[level].empty()) {
                ptr = nodeQueues[level].front();
                nodeQueues[level].pop();
                if (ptr->left != NULL) nodeQueues[1 - level].push(ptr->left);
                if (ptr->right != NULL) nodeQueues[1 - level].push(ptr->right);
            }
            level = 1 - level;
        }
        return leftPtr->val;
    }
};

int main() {
    Solution solution;
    TreeNode* root = new TreeNode(1);
    root->left = new TreeNode(2);
    root->right = new TreeNode(3);
    root->left->left = new TreeNode(4);
    root->right->left = new TreeNode(5);
    root->right->right = new TreeNode(6);
    root->right->left->left = new TreeNode(7);
    cout << solution.findBottomLeftValue(root);
    return 0;
}