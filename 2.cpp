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
    ListNode *addTwoNumbers(ListNode *l1, ListNode *l2) {
        int c = 0;
        ListNode *ans = NULL;
        ListNode *ptr = NULL;
        do {
            if (ans == NULL) {
                ans = new ListNode(0);
                ptr = ans;
            } else {
                ptr->next = new ListNode(0);
                ptr = ptr->next;
            }
            int a = l1 == NULL ? 0 : l1->val;
            int b = l2 == NULL ? 0 : l2->val;
            int sum = a + b + c;
            c = sum >= 10 ? 1 : 0;
            ptr->val = sum % 10;
            l1 = l1 == NULL ? NULL : l1->next;
            l2 = l2 == NULL ? NULL : l2->next;
        } while (l1 != NULL || l2 != NULL || c != 0);
        return ans;
    }
};

int main() {
    Solution solution;
    ListNode *l1 = new ListNode(2);
    l1->next = new ListNode(4);
    l1->next->next = new ListNode(3);
    ListNode *l2 = new ListNode(5);
    l2->next = new ListNode(6);
    l2->next->next = new ListNode(4);
    ListNode *ptr = solution.addTwoNumbers(l1, l2);
    while (ptr != NULL) {
        cout << ptr->val << ' ';
        ptr = ptr->next;
    }
}