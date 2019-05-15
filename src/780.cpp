//
// Created by linkinpark213 on 5/15/19.
//
#include <iostream>

using namespace std;

class Solution {
public:
    bool reachingPoints(int sx, int sy, int tx, int ty) {
        if (sx == tx && sy == ty) return true;
        if (tx == ty || tx < sx || ty < sy)
            return false;
        else if (tx < ty) {
            int temp = ty % tx;
            while (temp < sy && temp < ty - tx) {
                temp += tx;
            }
            return reachingPoints(sx, sy, tx, temp);
        } else {
            int temp = tx % ty;
            while (temp < sx && temp < tx - ty) {
                temp += ty;
            }
            return reachingPoints(sx, sy, temp, ty);
        }
    }
};

int main() {
    Solution solution;
    cout << solution.reachingPoints(9, 5, 12, 8);
    cout << solution.reachingPoints(9, 10, 9, 19);
    cout << solution.reachingPoints(10, 5, 15, 5);
    cout << solution.reachingPoints(1, 1, 3, 5);
}