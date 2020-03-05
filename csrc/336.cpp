//
// Created by linkinpark213 on 5/21/19.
//
#include <iostream>
#include <vector>

using namespace std;

class Solution {
    bool arePalindromePair(string &s1, string &s2) {
        int l1 = s1.length();
        int l2 = s2.length();
        char c1, c2;
        int limit = (l1 + l2) / 2;
        for (int i = 0; i < limit; i++) {
            c1 = i < l1 ? s1[i] : s2[i - l1];
            c2 = i < l2 ? s2[l2 - i - 1] : s1[l1 - i + l2 - 1];
            if (c1 != c2) return false;
        }
        return true;
    }

public:
    vector<vector<int>> palindromePairs(vector<string> &words) {
        vector<vector<int>> pairs;
        for (int i = 0; i < words.size(); i++) {
            for (int j = 0; j < words.size(); j++) {
                if (i != j)
                    if (this->arePalindromePair(words[i], words[j])) {
                        vector<int> pair;
                        pair.push_back(i);
                        pair.push_back(j);
                        pairs.push_back(pair);
                    }
            }
        }
        return pairs;
    }
};

int main() {
    Solution solution;
    string strings[] = {"abcd", "dcba", "lls", "s", "sssll"};
    vector<string> words(strings, strings + sizeof(strings) / sizeof(string));
    vector<vector<int>> pairs = solution.palindromePairs(words);

    for (vector<int> &v : pairs) {
        for (auto i : v) {
            cout << i << " ";
        }
        cout << endl;
    }
    return 0;
}