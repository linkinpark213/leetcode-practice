//
// Created by linkinpark213 on 5/6/19.
//

#include <iostream>
#include <algorithm>

using namespace std;

class Solution {
public:
    string reverseWords(string s) {
        string ans = "";
        string word = "";
        bool first = true;
        bool more = false;
        for (int i = s.size() - 1; i >= 0; i--) {
            if (s[i] != ' ') {
                more = true;
                word.append(1, s[i]);
            } else {
                if (more) {
                    if (!first) {
                        ans.append(1, ' ');
                    }
                    reverse(word.begin(), word.end());
                    ans.append(word);
                    word = "";
                    first = false;
                }
                more = false;
            }
        }
        if (word.size() > 0) {
            if (!first) {
                ans.append(1, ' ');
            }
            reverse(word.begin(), word.end());
            ans.append(word);
        }
        return ans;
    }
};

int main() {
    Solution solution;
    cout << solution.reverseWords("a good  example");
}