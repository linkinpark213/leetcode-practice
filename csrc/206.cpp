//
// Created by linkinpark213 on 6/8/19.
//
#include <iostream>
#include <stack>

using namespace std;

struct ListNode {
    int val;
    ListNode *next;

    ListNode(int x) : val(x), next(NULL) {}
};

class Solution {
public:
    ListNode *reverseList(ListNode *head) {
        ListNode *ptr = NULL, *prev = NULL;
        stack<ListNode *> stack;
        while (head != NULL) {
            stack.push(head);
            head = head->next;
        }
        while (!stack.empty()) {
            ptr = stack.top();
            stack.pop();
            if (prev != NULL) prev->next = ptr;
            else head = ptr;
            if (stack.empty()) ptr->next = NULL;
            prev = ptr;
        }
        return head;
    }
};

int main() {
    Solution solution;
    ListNode *root = new ListNode(1);
    root->next = new ListNode(2);
    root->next->next = new ListNode(3);
    root->next->next->next = new ListNode(4);
    root->next->next->next->next = new ListNode(5);
    ListNode *ans = solution.reverseList(root);
    while (ans != NULL) {
        cout << ans->val << " ";
        ans = ans->next;
    }
}