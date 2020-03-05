//
// Created by linkinpark213 on 6/22/19.
//

#include <iostream>
#include <vector>
#include <stack>

using namespace std;

class Solution {
public:
    string reverseWords(string s) {
        string ans;
        auto *chars = new stack<char>();
        for (char i : s) {
            if (i == ' ') {
                while (!chars->empty()) {
                    ans.push_back(chars->top());
                    chars->pop();
                }
                ans.push_back(' ');
            } else {
                chars->push(i);
            }
        }
        while (!chars->empty()) {
            ans.push_back(chars->top());
            chars->pop();
        }
        return ans;
    }
};

int main() {
    Solution solution;
    cout << solution.reverseWords("Let's take LeetCode contest");
}