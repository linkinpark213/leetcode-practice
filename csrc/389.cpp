//
// Created by linkinpark213 on 5/27/19.
//
#include <iostream>
#include <string>

using namespace std;

class Solution {
public:
    char findTheDifference(string s, string t) {
        char ans = 0;
        for (char c : s) {
            ans ^= c;
        }
        for (char c : t) {
            ans ^= c;
        }
        return ans;
    }
};

int main() {
    Solution solution;
    cout << solution.findTheDifference("abcd", "abcde");
}