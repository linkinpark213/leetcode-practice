#include <iostream>

using namespace std;

class Solution {
public:
    int integerBreak(int n) {
        if (n <= 3) return n - 1;
        int memo[n];
        for (int i = 0; i < n; i++) memo[i] = i + 1;
        for (int i = 3; i < n; i++) {
            for (int j = 0; j < i; j++) {
                memo[i] = max(memo[i], memo[j] * memo[i - j - 1]);
            }
        }
        return memo[n - 1];
    }
};

int main() {
    Solution solution;
    cout << solution.integerBreak(2) << endl;
    cout << solution.integerBreak(3) << endl;
    cout << solution.integerBreak(6) << endl;
    cout << solution.integerBreak(10) << endl;
}