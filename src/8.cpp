//
// Created by linkinpark213 on 5/6/19.
//

#include <iostream>

#define INT_MAX 2147483647
#define INT_MIN (-INT_MAX - 1)
using namespace std;

class Solution {
public:
    int myAtoi(string str) {
        bool positive = true;
        int ans = 0;
        bool begun = false;
        for (int i = 0; i < str.size(); i++) {
            char c = str[i];
            if (c == ' ') {
                if (begun == false)
                    continue;
                else
                    break;
            } else if (c == '+') {
                if (!begun) {
                    positive = true;
                    begun = true;
                } else {
                    return ans;
                }
            } else if (c == '-') {
                if (!begun) {
                    positive = false;
                    begun = true;
                } else {
                    return ans;
                }
            } else if (c >= '0' && c <= '9') {
                int r = c - '0';
                if (ans <= INT_MAX / 10 && ans >= INT_MIN / 10) {
                    ans *= 10;
                } else if (ans < INT_MIN / 10) {
                    return INT_MIN;
                } else if (ans > INT_MAX / 10) {
                    return INT_MAX;
                }
                if (positive) {
                    if (ans <= INT_MAX - r) {
                        ans += r;
                    } else {
                        return INT_MAX;
                    }
                } else {
                    if (ans >= INT_MIN + r) {
                        ans -= r;
                    } else {
                        return INT_MIN;
                    }
                }
                if (!begun) {
                    begun = true;
                }
            } else {
                break;
            }
        }
        return ans;
    }
};

int main() {
    Solution solution;
    cout << solution.myAtoi("   -42");
}