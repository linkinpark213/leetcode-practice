//
// Created by linkinpark213 on 5/6/19.
//

#include <iostream>

using namespace std;

class Solution {
public:
    int strStr(string haystack, string needle) {
        if (needle.size() == 0) return 0;
        if (haystack.size() == 0) return -1;
        if (needle.size() > haystack.size()) return -1;
        for (int i = 0; i < haystack.size() - needle.size() + 1; i++) {
            bool consistent = true;
            for (int j = 0; j < needle.size(); j++) {
                if (haystack[i + j] != needle[j]) consistent = false;
            }
            if (consistent == true) return i;
        }
        return -1;
    }
};

int main() {
    Solution solution;
    cout << solution.strStr("hello", "ll");
}