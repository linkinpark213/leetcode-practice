//
// Created by linkinpark213 on 5/6/19.
//

#include <iostream>

#define INT_MAX 2147483647
#define INT_MIN (-INT_MAX - 1)
using namespace std;

class Solution {
public:
    int reverse(int x) {
        if (x == INT_MAX || x == INT_MIN)
            return 0;
        bool positive = x > 0;
        int temp = positive ? x : -x;
        int ans = 0;
        while (temp > 0) {
            int r = temp % 10;
            temp = (temp - r) / 10;
            if (ans > INT_MAX / 10) {
                return 0;
            }
            ans *= 10;
            ans += r;
        }
        return ans * (positive ? 1 : -1);
    }
};

int main() {
    Solution solution;
    cout << solution.reverse(-123);
}