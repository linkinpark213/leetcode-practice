//
// Created by linkinpark213 on 5/30/19.
//

#include <iostream>
#include <vector>

using namespace std;


// Definition for a Node.
class Node {
public:
    int val;
    vector<Node *> children;

    Node() {}

    Node(int _val, vector<Node *> _children) {
        val = _val;
        children = _children;
    }
};

class Solution {
    vector<int> addChildren(Node *root, vector<int> &traversal) {
        for (Node *child:root->children) {
            addChildren(child, traversal);
        }
        traversal.push_back(root->val);
        return traversal;
    }

public:
    vector<int> postorder(Node *root) {
        vector<int> traversal;
        if (root != NULL)
            addChildren(root, traversal);
        return traversal;
    }
};

int main() {
    Solution solution;
    Node root(1, vector<Node *>());
    Node a(3, vector<Node *>());
    Node b(2, vector<Node *>());
    Node c(4, vector<Node *>());
    Node d(5, vector<Node *>());
    Node e(6, vector<Node *>());
    root.children.push_back(&a);
    root.children.push_back(&b);
    root.children.push_back(&c);
    a.children.push_back(&d);
    a.children.push_back(&e);
    vector<int> traversal = solution.postorder(&root);
    for (int i : traversal) {
        cout << i << " ";
    }
}