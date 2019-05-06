//
// Created by linkinpark213 on 5/6/19.
//
#include <iostream>

using namespace std;

class Solution {
public:
    int lengthOfLongestSubstring(string s) {
        int max_length = 0;
        string substr;
        for (int i = 0; i < s.size(); i++) {
            substr = "";
            for (int j = i; j < s.size(); j++) {
                int pos = substr.find(s[j]);
                if (pos >= 0 && pos < j - i) {
                    break;
                }
                substr.push_back(s[j]);
                max_length = max(max_length, j - i + 1);
            }
        }
        return max_length;
    }
};

int main() {
    Solution solution;
    cout << solution.lengthOfLongestSubstring("abcabcbb");
}