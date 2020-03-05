//
// Created by linkinpark213 on 6/8/19.
//

#include <iostream>
#include <string>

using namespace std;

class Solution {
public:
    int characterReplacement(string s, int k) {
        char c;
        int n, l, max_l = 0, length = s.length();
        for (int i = 0; i < length; i++) {
            c = s[i];
            n = 0;
            l = 1;
            for (int j = i + 1; n <= k; j++) {
                if (j == length) {
                    l += (k - n);
                    if (l > length) l = length;
                    break;
                }
                if (s[j] != c) {
                    if (n < k) l++;
                    n++;
                } else {
                    if (n == 0) i++;
                    l++;
                }
            }
            if (max_l < l) max_l = l;
        }
        return max_l;
    }
};

int main() {
    Solution solution;
    cout << solution.characterReplacement("ABAB", 2) << endl;
    cout << solution.characterReplacement("AABABBA", 1) << endl;
    cout << solution.characterReplacement("ABBB", 2) << endl;
}
