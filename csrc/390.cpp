//
// Created by linkinpark213 on 5/29/19.
//

#include <iostream>
#include <vector>

using namespace std;

class Solution {
public:
    int lastRemaining(int n) {
        if (n == 1) return 1;
        else if (n <= 3) return 2;
        else {
            if ((n / 2) % 2 == 1) {
                return 4 * lastRemaining((n - 2) / 4);
            } else {
                return 4 * lastRemaining(n / 4) - 2;
        }
        }
    }
};

int main() {
    Solution solution;
    cout << solution.lastRemaining(9);
}