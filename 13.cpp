//
// Created by linkinpark213 on 5/6/19.
//

#include <iostream>

using namespace std;

class Solution {
    int singleRomanToInt(char c) {
        switch (c) {
            case 'I':
                return 1;
            case 'V':
                return 5;
            case 'X':
                return 10;
            case 'L':
                return 50;
            case 'C':
                return 100;
            case 'D':
                return 500;
            case 'M':
                return 1000;
            default:
                return 0;
        }
    }

public:
    int romanToInt(string s) {
        int total = 0;
        int prev = 0, curr = 0;
        for (int i = 0; i <= s.size(); i++) {
            if (i > 0) prev = curr;
            if (i < s.size()) curr = singleRomanToInt(s[i]);
            if (curr <= prev) {
                total += prev;
            } else {
                total -= prev;
            }
        }
        return total;
    }
};

int main() {
    Solution solution;
    cout << solution.romanToInt("LVIII");
}