//
// Created by linkinpark213 on 5/6/19.
//

#include <iostream>
#include <vector>

using namespace std;

class Solution {
public:
    string longestCommonPrefix(vector<string> &strs) {
        string substr = "";
        int n = 0;
        if (strs.size() > 0)
            while (n < strs[0].size()) {
                char c = strs[0][n];
                bool consistent = true;
                for (int i = 1; i < strs.size(); i++) {
                    if (n == strs[i].size()) return substr;
                    if (c != strs[i][n]) consistent = false;
                }
                if (consistent) {
                    substr.push_back(c);
                    n++;
                } else break;
            }
        return substr;
    }
};

int main() {
    Solution solution;
    vector<string> strs;
    strs.push_back("flower");
    strs.push_back("flow");
    strs.push_back("flight");
    cout << solution.longestCommonPrefix(strs);
}