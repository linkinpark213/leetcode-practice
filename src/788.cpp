//
// Created by linkinpark213 on 5/21/19.
//
#include <iostream>
#include <vector>

using namespace std;

class Solution {
    bool isValid(int N) {
        int temp = N;
        int r = 0;
        bool valid = false;
        while (temp > 0) {
            r = temp % 10;
            temp = temp / 10;
            switch (r) {
                case 2:
                case 5:
                case 6:
                case 9:
                    valid = true;
                    break;
                case 3:
                case 4:
                case 7:
                    return false;
                default:
                    continue;
            }
        }
        return valid;
    }

public:
    int rotatedDigits(int N) {
        int sum = 0;
        for (int i = 2; i <= N; i++) {
            if (isValid(i)) {
                sum++;
            };
        }
        return sum;
    }
};

int main() {
    Solution solution;
    cout << solution.rotatedDigits(857);
}