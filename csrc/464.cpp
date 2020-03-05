#include <iostream>
#include <vector>
#include <unordered_map>

using namespace std;

class Solution {
    bool canIWinHelper(int maxChoosableInteger, int desiredTotal, int state, unordered_map<int, bool>& memo) {
        if (memo.find(state) != memo.end()) return memo.find(state)->second;
        bool canWin = false;
        for (int i = maxChoosableInteger; i > 0; i--) {
            if (((state >> i) & 1) != 1) {
                if (i >= desiredTotal) canWin = true;
                else {
                    canWin = !canIWinHelper(maxChoosableInteger, desiredTotal - i, state | (1 << i), memo);
                }
            }
            if (canWin) break;
        }
        memo.insert(pair<int, bool>(state, canWin));
        return canWin;
    }
public:
    bool canIWin(int maxChoosableInteger, int desiredTotal) {
        if (maxChoosableInteger * (maxChoosableInteger + 1) / 2 < desiredTotal) return false;
        unordered_map<int, bool> memo;
        return canIWinHelper(maxChoosableInteger, desiredTotal, 0, memo);
    }
};

int main() {
    Solution solution;
    cout << !solution.canIWin(10, 11) << endl;
    cout << solution.canIWin(10, 1) << endl;
    cout << solution.canIWin(3, 5) << endl;
    cout << !solution.canIWin(10, 40) << endl;
    cout << solution.canIWin(11, 25) << endl;
    return 0;
}