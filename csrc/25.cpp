//
// Created by linkinpark213 on 5/6/19.
//

#include <iostream>
#include <vector>

using namespace std;

struct ListNode {
    int val;
    ListNode *next;

    ListNode(int x) : val(x), next(NULL) {}
};

class Solution {
    void getNextSubGroup(vector<ListNode *> &ptrs, ListNode *ptr, int k) {
        ptrs.clear();
        for (int i = 0; i < k; i++) {
            if (ptr == NULL) return;
            ptrs.push_back(ptr);
            ptr = ptr->next;
        }
    }

public:
    ListNode *reverseKGroup(ListNode *head, int k) {
        ListNode *newhead = head;
        ListNode *ptr = head;
        ListNode *prev = NULL, *next;
        vector<ListNode *> ptrs;
        while (true) {
            getNextSubGroup(ptrs, ptr, k);
            if (ptrs.size() == k) {
                next = ptrs[k - 1]->next;
                if (prev != NULL) prev->next = ptrs[k - 1];
                for (int i = k - 1; i > 0; i--) {
                    ptrs[i]->next = ptrs[i - 1];
                }
                ptrs[0]->next = next;
                prev = ptrs[0];
                ptr = prev->next;
                if (newhead == ptrs[0]) newhead = ptrs[k - 1];
            } else {
                break;
            }
        }
        return newhead;
    }
};

int main() {
    Solution solution;
    ListNode *head = new ListNode(1);
    head->next = new ListNode(2);
    head->next->next = new ListNode(3);
    head->next->next->next = new ListNode(4);
    head->next->next->next->next = new ListNode(5);
    ListNode *ptr = solution.reverseKGroup(head, 3);
    while (ptr != NULL) {
        cout << ptr->val << ' ';
        ptr = ptr->next;
    }
}