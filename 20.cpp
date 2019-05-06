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

class Stack {
    char value;
    ListNode *top = NULL;
public:
    void push(char c) {
        ListNode *temp = new ListNode(c);
        temp->next = top;
        top = temp;
    }

    char pop() {
        if (this->size() == 0) return ' ';
        else {
            char c = top->val;
            top = top->next;
            return c;
        }
    }

    int size() {
        int count = 0;
        ListNode *ptr = top;
        while (ptr != NULL) {
            count++;
            ptr = ptr->next;
        }
        return count;
    }
};

class Solution {
public:
    bool isValid(string s) {
        Stack st;
        char c, prev_c;
        for (int i = 0; i < s.size(); i++) {
            c = s[i];
            switch (c) {
                case '(':
                case '[':
                case '{':
                    st.push(c);
                    break;
                case ')':
                    prev_c = st.pop();
                    if (prev_c != '(')
                        return false;
                    break;
                case ']':
                    prev_c = st.pop();
                    if (prev_c != '[')
                        return false;
                    break;
                case '}':
                    prev_c = st.pop();
                    if (prev_c != '{')
                        return false;
                    break;
            }
        }
        if (st.size() == 0)
            return true;
        return false;
    }
};

int main() {
    Solution solution;
    cout << solution.isValid("(){}[]");
}