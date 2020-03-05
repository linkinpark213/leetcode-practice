#include <iostream>
#include <map>

using namespace std;

struct TreeNode {
     int val;
     TreeNode *left;
     TreeNode *right;
     TreeNode(int x) : val(x), left(NULL), right(NULL) {}
};

struct Memo {
    int maxRobbed;
    int maxUnrobbed;
    Memo(int x, int y) : maxRobbed(x), maxUnrobbed(y) {}
};

class Solution {
public:
    int robWithMemos(TreeNode* node, map<TreeNode*, Memo> &memos, bool canRob) {
        auto iterator = memos.find(node);
        if (iterator == memos.end()) {
            int valueRobbed = node->val;
            if (node->left != NULL)
                valueRobbed += robWithMemos(node->left, memos, false);
            if (node->right != NULL)
                valueRobbed += robWithMemos(node->right, memos, false);

            int valueUnrobbed = 0;
            if (node->left != NULL)
                valueUnrobbed += robWithMemos(node->left, memos, true);
            if (node->right != NULL)
                valueUnrobbed += robWithMemos(node->right, memos, true);
            memos.insert(pair(node, Memo(valueRobbed, valueUnrobbed)));
            return canRob ? max(valueRobbed, valueUnrobbed) : valueUnrobbed;
        } else {
            auto record = iterator->second;
            return canRob ? max(record.maxRobbed, record.maxUnrobbed) : record.maxUnrobbed;
        }
        return 0;
    }

    int rob(TreeNode* root) {
        if (root == NULL) {
            return 0;
        }
        map<TreeNode*, Memo> memos;
        int valueRobbed = robWithMemos(root, memos, true);
        int valueUnrobbed = robWithMemos(root, memos, false);
        return max(valueRobbed, valueRobbed);
    }
};

int main() {
    Solution solution;
    TreeNode* root = new TreeNode(3);
    root->left = new TreeNode(4);
    root->right = new TreeNode(5);
    root->left->left = new TreeNode(1);
    root->left->right = new TreeNode(3);
    root->right->right = new TreeNode(1);
    cout << solution.rob(root);
    return 0;
}