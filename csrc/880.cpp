//
// Created by linkinpark213 on 5/6/19.
//
#include <iostream>

using namespace std;

class Solution {
public:
    string decodeAtIndex(string S, int K) {
        int lastcharpos = 0;
        int currentpos = 0;
        int repeat = 1;
        long i = 0;
        char c;
        while (i < K) {
            c = S[currentpos];
            if (c >= 'a' && c <= 'z') {
                lastcharpos = currentpos;
                i += 1;
            } else if (c >= '2' && c <= '9') {
                repeat = c - '0';
                if (i * repeat > K) {
                    int r = K % i;
                    if (r == 0)
                        return string(1, S[lastcharpos]);
                    else
                        return decodeAtIndex(S, r);
                } else if (i * repeat == K) {
                    return string(1, S[lastcharpos]);
                } else {
                    i *= repeat;
                }
            }
            currentpos++;
        }
        return string(1, S[lastcharpos]);
    }
};

int main() {
    Solution solution;
    cout << solution.decodeAtIndex(
            "vk6u5xhq9v",
            554
    );
}