#include <iostream>

using namespace std;

class Solution {
public:
    double nthPersonGetsNthSeat(int n) {
        if (n == 1) return 1.0;
        return (1.0 / n) + ((n - 2.0) / n) * nthPersonGetsNthSeat(n - 1);
    }
};

int main() {
    Solution solution;
    cout << solution.nthPersonGetsNthSeat(4);
    return 0;
}