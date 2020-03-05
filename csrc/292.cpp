//
// Created by linkinpark213 on 6/23/19.
//

#include <iostream>

using namespace std;

class Solution {
public:
    bool canWinNim(int n) {
        return n >> 2 << 2 != n;
    }
};

int main() {
    Solution solution;
    cout << solution.canWinNim(4);
}