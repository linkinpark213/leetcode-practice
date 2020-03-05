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
    ListNode *swapPairs(ListNode *head) {
        if (head == NULL) return NULL;
        ListNode *ptr0, *ptr1, *ptr2, *temp;
        ptr1 = head;
        if (ptr1->next == NULL) return ptr1;
        ptr2 = ptr1->next;
        ptr0 = ptr2;
        temp = NULL;
        while (ptr1 != NULL && ptr2 != NULL) {
            ptr1->next = ptr2->next;
            ptr2->next = ptr1;
            if (temp != NULL) temp->next = ptr2;
            temp = ptr1;
            ptr1 = ptr1->next;
            if (ptr1 != NULL) ptr2 = ptr1->next;
            else ptr2 = NULL;
        }
        return ptr0;
    }
};

int main() {
    Solution solution;
    ListNode *head = new ListNode(1);
    head->next = new ListNode(2);
    head->next->next = new ListNode(3);
    head->next->next->next = new ListNode(4);
    ListNode *ptr = solution.swapPairs(head);
    while (ptr != NULL) {
        cout << ptr->val << ' ';
        ptr = ptr->next;
    }
}