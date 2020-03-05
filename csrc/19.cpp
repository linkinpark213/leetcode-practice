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
    ListNode *removeNthFromEnd(ListNode *head, int n) {
        int count = 0;
        ListNode *ptr = head;
        while (ptr != NULL) {
            count++;
            ptr = ptr->next;
        }
        int target = count - n;
        ptr = head;
        for (int i = 0; i < target - 1; i++) {
            ptr = ptr->next;
        }
        if (target == 0) {
            return ptr->next;
        }
        ListNode *toRemove = ptr->next;
        ListNode *cont;
        if (toRemove != NULL)
            cont = toRemove->next;
        else
            cont = NULL;
        ptr->next = cont;
        return head;
    }
};

int main() {
    Solution solution;
    ListNode *head = new ListNode(1);
    head->next = new ListNode(2);
    head->next->next = new ListNode(3);
    head->next->next->next = new ListNode(4);
    head->next->next->next->next = new ListNode(5);
    ListNode *ptr = solution.removeNthFromEnd(head, 2);
    while (ptr != NULL) {
        cout << ptr->val << ' ';
        ptr = ptr->next;
    }
}