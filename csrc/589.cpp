#include <iostream>
#include <vector>
#include <queue>

using namespace std;

// Definition for a Node.
class Node {
public:
    int val;
    vector<Node*> children;

    Node() {}

    Node(int _val) {
        val = _val;
    }

    Node(int _val, vector<Node*> _children) {
        val = _val;
        children = _children;
    }
};

class Solution {
public:
    vector<int> preorder(Node* root) {
        vector<int> reordered;
        if (root == NULL) return reordered;
        queue<Node*> nodeQueue;
        nodeQueue.push(root);
        while (!nodeQueue.empty()) {
            Node* node = nodeQueue.front();
            nodeQueue.pop();
            reordered.push_back(node->val);
            for (int i = 0; i < node->children.size(); i++)
                nodeQueue.push(node->children[i]);
        }
        return reordered;
    }
};

int main() {
    Solution solution;
    Node* root = new Node(1);
    root->children.push_back(new Node(3));
    root->children.push_back(new Node(2));
    root->children.push_back(new Node(4));
    root->children[0]->children.push_back(new Node(5));
    root->children[0]->children.push_back(new Node(6));
    auto ans = solution.preorder(root);
    for (auto it = ans.begin(); it != ans.end(); it++) {
        cout << *it << " ";
    }
    return 0;
}