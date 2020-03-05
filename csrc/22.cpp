//
// Created by linkinpark213 on 6/5/19.
//
#include <iostream>
#include <vector>

using namespace std;

class Solution {
public:
    vector<string> generateParenthesis(int n) {
        if (n < 1) {
            return vector<string>(1, "");
        } else if (n == 1)
            return vector<string>(1, "()");
        else {
            vector<string> ans;
            for (int i = 0; i < n; i++) {
                vector<string> left = generateParenthesis(i);
                vector<string> right = generateParenthesis(n - i - 1);
                for (const string &l : left) {
                    for (const string &r : right) {
                        string s = "(";
                        s += l;
                        s += ")";
                        s += r;
                        ans.push_back(s);
                    }
                }
            }
            return ans;
        }
    }
};

int main(int argc, char **argv) {
    Solution solution;
    vector<string> ans = solution.generateParenthesis(4);
    for (const auto &s : ans) {
        cout << s << endl;
    }
    cout << ans.size();
}