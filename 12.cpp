//
// Created by linkinpark213 on 5/6/19.
//

#include <iostream>

using namespace std;

class Solution {
public:
    string intToRoman(int num) {
        string ans = "";
        int temp = num;
        int d, r;
        int units[] = {1000, 500, 100, 50, 10, 5, 1};
        char symbols[] = {'M', 'D', 'C', 'L', 'X', 'V', 'I'};
        for (int i = 0; i < 7; i += 2) {
            d = temp / units[i];
            temp -= units[i] * d;
            switch (d) {
                case 0:
                    break;
                case 3:
                    ans.push_back(symbols[i]);
                case 2:
                    ans.push_back(symbols[i]);
                case 1:
                    ans.push_back(symbols[i]);
                    break;
                case 4:
                    ans.push_back(symbols[i]);
                case 5:
                    ans.push_back(symbols[i - 1]);
                    break;
                case 6:
                    ans.push_back(symbols[i - 1]);
                    ans.push_back(symbols[i]);
                    break;
                case 7:
                    ans.push_back(symbols[i - 1]);
                    ans.push_back(symbols[i]);
                    ans.push_back(symbols[i]);
                    break;
                case 8:
                    ans.push_back(symbols[i - 1]);
                    ans.push_back(symbols[i]);
                    ans.push_back(symbols[i]);
                    ans.push_back(symbols[i]);
                    break;
                case 9:
                    ans.push_back(symbols[i]);
                    ans.push_back(symbols[i - 2]);
                    break;
            }
        }
        return ans;
    }
};

int main() {
    Solution solution;
    cout << solution.intToRoman(58);
}