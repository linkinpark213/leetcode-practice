//
// Created by linkinpark213 on 5/6/19.
//

#include <iostream>
#include <vector>

using namespace std;

class Solution {
public:
    bool isPalindrome(int x) {
        if (x < 0) return false;
        int temp = x;
        vector<int> rev;
        while (temp > 0) {
            int r = temp % 10;
            temp = temp - r;
            temp /= 10;
            rev.push_back(r);
        }
        int size = rev.size();
        for (int i = 0; i < size / 2; ++i) {
            if (rev[i] != rev[size - i - 1]) {
                return false;
            }
        }
        return true;
    }
};

int main() {
    Solution solution;
    cout << solution.isPalindrome(121);
}