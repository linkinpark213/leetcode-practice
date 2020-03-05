//
// Created by linkinpark213 on 7/21/19.
//
#include <iostream>
#include <math.h>

using namespace std;

class Solution {
public:
    bool judgeSquareSum(int c) {
        int upper_bound = int(sqrt(c / 2));
        double b;
        for (int i = 0; i <= upper_bound; i++) {
            b = sqrt(c - i * i);
            if (b == int(b)) {
                return true;
            }
        }
        return false;
    }
};

int main() {
    Solution solution;
    cout << solution.judgeSquareSum(5);
    cout << solution.judgeSquareSum(3);
    cout << solution.judgeSquareSum(8);
    cout << solution.judgeSquareSum(2147482647);
}