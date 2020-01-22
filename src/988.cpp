#include <iostream>
#include <vector>

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
    bool smaller(vector<int>& a, vector<int>& b) {
        int ptra = a.size() - 1;
        int ptrb = b.size() - 1;
        if (ptra == -1) return false;
        if (ptrb == -1) return true;
        while (ptra != -1 && ptrb != -1) {
            if (a[ptra] < b[ptrb]) return true;
            else if (a[ptra] > b[ptrb]) return false;
            ptra--;
            ptrb--;
        }
        if (ptra == -1) return true;
        return false; 
    }

    vector<int> smallestIntFromLeaf(TreeNode* node, vector<int>& curr, vector<int>& minValue) {
        curr.push_back(node->val);
        if (node->left == NULL && node->right == NULL) {
            if (smaller(curr, minValue)) {
                minValue = curr;
            }
        } else {
            if (node->left != NULL) {
                vector<int> temp = smallestIntFromLeaf(node->left, curr, minValue);
                if (smaller(temp, minValue)) minValue = temp;
            }
            if (node->right != NULL) {
                vector<int> temp = smallestIntFromLeaf(node->right, curr, minValue);
                if (smaller(temp, minValue)) minValue = temp;
            }
        }
        curr.pop_back();
        return minValue;
    }
public:
    string smallestFromLeaf(TreeNode* root) {
        if (root == NULL) return "";
        vector<int> curr;
        vector<int> minValue;
        vector<int> smallestSeq = smallestIntFromLeaf(root, curr, minValue);
        string ans = "";
        int ptr = smallestSeq.size() - 1;
        while (ptr != -1) {
            ans += char(smallestSeq[ptr] + 'a');
            ptr--;
        }
        return ans;
    }
};

int main() {
    Solution solution;
    TreeNode *root = new TreeNode(25);
    root->left = new TreeNode(1);
    root->right = new TreeNode(3);
    root->left->left = new TreeNode(1);
    root->left->right = new TreeNode(3);
    root->right->left = new TreeNode(0);
    root->right->right = new TreeNode(2);
    cout << solution.smallestFromLeaf(root);
}