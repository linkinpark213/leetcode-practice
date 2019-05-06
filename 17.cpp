//
// Created by linkinpark213 on 5/6/19.
//

#include <iostream>
#include <vector>

using namespace std;

class Solution {
    vector<char> letters(char digit) {
        switch (digit) {
            case '2': {
                char a[] = {'a', 'b', 'c'};
                return vector<char>(a, a + sizeof(a) / sizeof(char));
            }
            case '3': {
                char a[] = {'d', 'e', 'f'};
                return vector<char>(a, a + sizeof(a) / sizeof(char));
            }
            case '4': {
                char a[] = {'g', 'h', 'i'};
                return vector<char>(a, a + sizeof(a) / sizeof(char));
            }
            case '5': {
                char a[] = {'j', 'k', 'l'};
                return vector<char>(a, a + sizeof(a) / sizeof(char));
            }
            case '6': {
                char a[] = {'m', 'n', 'o'};
                return vector<char>(a, a + sizeof(a) / sizeof(char));
            }
            case '7': {
                char a[] = {'p', 'q', 'r', 's'};
                return vector<char>(a, a + sizeof(a) / sizeof(char));
            }
            case '8': {
                char a[] = {'t', 'u', 'v'};
                return vector<char>(a, a + sizeof(a) / sizeof(char));
            }
            case '9': {
                char a[] = {'w', 'x', 'y', 'z'};
                return vector<char>(a, a + sizeof(a) / sizeof(char));
            }
            default:
                return vector<char>();
        }
    }

public:
    vector<string> letterCombinations(string digits) {
        vector<string> strs;
        vector<char> ls = letters(digits[0]);
        if (digits.size() == 0) {
            return strs;
        } else if (digits.size() == 1) {
            for (int i = 0; i < ls.size(); i++) {
                strs.push_back(string(1, ls[i]));
            }
        } else {
            string following_digits = string(digits).erase(0, 1);
            vector<string> suffices = letterCombinations(following_digits);
            for (int i = 0; i < ls.size(); i++) {
                for (int j = 0; j < suffices.size(); j++) {
                    strs.push_back(string(suffices[j]).insert(0, 1, ls[i]));
                }
            }
        }
        return strs;
    }
};

int main() {
    Solution solution;
    for (string s : solution.letterCombinations("23")) {
        cout << s << ' ';
    }
}