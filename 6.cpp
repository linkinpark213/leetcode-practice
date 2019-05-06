//
// Created by linkinpark213 on 5/6/19.
//

#include <iostream>

using namespace std;

class Solution {
public:
    string convert(string s, int numRows) {
        if (s.size() <= 2) return s;
        string ans = "";
        for (int i = 0; i < numRows; i++) {
            int pos = i;
            int step = numRows > 1 ? (numRows - i - 1) * 2 : 1;
            ans.push_back(s[pos]);
            while (true) {
                if (pos + step < s.size()) {
                    if (step > 0) {
                        pos += step;
                        ans.push_back(s[pos]);
                    }
                } else break;
                if (pos + i * 2 < s.size()) {
                    if (i > 0) {
                        pos += i * 2;
                        ans.push_back(s[pos]);
                    }
                } else break;
            }
        }
        return ans;
    }
};

int main() {
    Solution solution;
    cout << solution.convert("PAYPALISHIRING", 3);
}