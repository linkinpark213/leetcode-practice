//
// Created by linkinpark213 on 6/3/19.
//

#include <iostream>

using namespace std;


struct ListNode {
    int val;
    ListNode *next;

    ListNode(int x) : val(x), next(NULL) {}
};


class Solution {
    ListNode *recursiveSort(ListNode *head, ListNode *former) {
        if (head == NULL || head->next == NULL)
            return head;
        ListNode *ptr = head, *min = head, *prev = former, *minPrev = former;
        while (ptr != NULL) {
            if (ptr->val < min->val) {
                min = ptr;
                minPrev = prev;
            }
            prev = ptr;
            ptr = ptr->next;
        }
        if (min != head) {
            if (former != NULL) {
                former->next = min;
            }
            minPrev->next = min->next;
            min->next = head;
        }
        recursiveSort(min->next, min);
        return min;
    }

public:
    ListNode *insertionSortList(ListNode *head) {
        return recursiveSort(head, NULL);
    }
};

int main() {
    Solution solution;
    ListNode *head = new ListNode(4);
    head->next = new ListNode(1);
    head->next->next = new ListNode(2);
    head->next->next->next = new ListNode(3);
    head = solution.insertionSortList(head);
    while (head != NULL) {
        cout << head->val << " ";
        head = head->next;
    }
    cout << endl;
    head = new ListNode(-1);
    head->next = new ListNode(5);
    head->next->next = new ListNode(3);
    head->next->next->next = new ListNode(4);
    head->next->next->next->next = new ListNode(0);
    head = solution.insertionSortList(head);
    while (head != NULL) {
        cout << head->val << " ";
        head = head->next;
    }
}