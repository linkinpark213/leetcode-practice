//
// Created by linkinpark213 on 5/6/19.
//

#include <iostream>

using namespace std;

struct ListNode {
    int val;
    ListNode *next;

    ListNode(int x) : val(x), next(NULL) {}
};

class Solution {
public:
    ListNode *mergeTwoLists(ListNode *l1, ListNode *l2) {
        ListNode *p1 = l1;
        ListNode *p2 = l2;
        ListNode *ans = new ListNode(-1);
        ListNode *head = ans;
        while (p1 != NULL || p2 != NULL) {
            if (p1 == NULL) {
                int v = p2->val;
                ans->next = new ListNode(v);
                ans = ans->next;
                p2 = p2->next;
            } else if (p2 == NULL) {
                int v = p1->val;
                ans->next = new ListNode(v);
                ans = ans->next;
                p1 = p1->next;
            } else {
                int v1 = p1->val;
                int v2 = p2->val;
                if (v1 < v2) {
                    int v = p1->val;
                    ans->next = new ListNode(v);
                    ans = ans->next;
                    p1 = p1->next;
                } else {
                    int v = p2->val;
                    ans->next = new ListNode(v);
                    ans = ans->next;
                    p2 = p2->next;
                }
            }

        }
        return head->next;
    }
};

int main() {
    Solution solution;
    ListNode *l1 = new ListNode(1);
    l1->next = new ListNode(2);
    l1->next->next = new ListNode(4);
    ListNode *l2 = new ListNode(1);
    l2->next = new ListNode(3);
    l2->next->next = new ListNode(4);
    ListNode *ptr = solution.mergeTwoLists(l1, l2);
    while (ptr != NULL) {
        cout << ptr->val << ' ';
        ptr = ptr->next;
    }
}