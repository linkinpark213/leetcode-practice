//
// Created by linkinpark213 on 2020/1/5.
//

#include <iostream>
using namespace std;

class Solution {
public:
    int minAddToMakeValid(string S) {
        int right = 0;
        int left = 0;
        int size = S.size();
        for (int i = 0; i < size; i++) {
            if (S[i] == '(')
                right++;
            else {
                if (right > 0)
                    right--;
                else
                    left++;
            }
        }
        return left + right;
    }
};

int main() {
    Solution solution;
    cout << solution.minAddToMakeValid("()");
    return 0;
}