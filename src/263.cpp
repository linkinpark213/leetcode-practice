#include <iostream>
#include <math.h>

using namespace std;

class Solution {
public:
    bool isUgly(int num) {
        if (num < 1) return false;
        while (num % 2 == 0 || num % 3 == 0 || num % 5 == 0) {
            if (num % 2 == 0) num = num / 2;
            if (num % 3 == 0) num = num / 3;
            if (num % 5 == 0) num = num / 5;
        }
        return num == 1;
    }
};

int main() {
    Solution solution;
    cout << solution.isUgly(6) << endl;
    cout << solution.isUgly(8) << endl;
    cout << solution.isUgly(14) << endl;
    return 0;
}