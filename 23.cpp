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
    ListNode *merge2Lists(ListNode *l1, ListNode *l2) {
        ListNode *ptr1 = l1;
        ListNode *ptr2 = l2;
        ListNode *head = new ListNode(0);
        ListNode *ptr = head;
        while (ptr1 != NULL || ptr2 != NULL) {
            if (ptr1 == NULL) {
                ptr->next = new ListNode(ptr2->val);
                ptr2 = ptr2->next;
                ptr = ptr->next;
            } else if (ptr2 == NULL) {
                ptr->next = new ListNode(ptr1->val);
                ptr1 = ptr1->next;
                ptr = ptr->next;
            } else {
                if (ptr1->val < ptr2->val) {
                    ptr->next = new ListNode(ptr1->val);
                    ptr1 = ptr1->next;
                    ptr = ptr->next;
                } else {
                    ptr->next = new ListNode(ptr2->val);
                    ptr2 = ptr2->next;
                    ptr = ptr->next;
                }
            }
        }
        return head->next;
    }

public:
    ListNode *mergeKLists(vector<ListNode *> &lists) {
        if (lists.size() == 0) return NULL;
        if (lists.size() == 1) return lists[0];
        while (lists.size() > 1) {
            for (int i = 1; i < lists.size(); i += 2) {
                lists[i] = merge2Lists(lists[i - 1], lists[i]);
            }
            if (lists.size() % 2 == 0) {
                for (int i = 0; i < lists.size(); i++) {
                    lists.erase(lists.begin() + i, lists.begin() + i + 1);
                }
            } else {
                for (int i = 0; i < lists.size() - 1; i++) {
                    lists.erase(lists.begin() + i, lists.begin() + i + 1);
                }
            }
        }
        return lists[0];
    }
};

int main() {
    Solution solution;
    ListNode *l1 = new ListNode(1);
    l1->next = new ListNode(4);
    l1->next->next = new ListNode(5);
    ListNode *l2 = new ListNode(1);
    l2->next = new ListNode(3);
    l2->next->next = new ListNode(4);
    ListNode *l3 = new ListNode(2);
    l3->next = new ListNode(6);
    vector<ListNode *> lists;
    lists.push_back(l1);
    lists.push_back(l2);
    lists.push_back(l3);
    ListNode *ptr = solution.mergeKLists(lists);
    while (ptr != NULL) {
        cout << ptr->val << ' ';
        ptr = ptr->next;
    }
}