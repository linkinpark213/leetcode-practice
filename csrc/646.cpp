#include <iostream>
#include <vector>

using namespace std;

class Solution {
public:
    int findLongestChain(vector<vector<int>>& pairs) {
        int temp[2];
        for (int i = 0; i < pairs.size(); i++) {
            for (int j = pairs.size() - 1; j > i; j--) {
                if (pairs[j][1] < pairs[j - 1][1]) {
                    temp[0] = pairs[j][0];
                    temp[1] = pairs[j][1];
                    pairs[j][0] = pairs[j - 1][0];
                    pairs[j][1] = pairs[j - 1][1];
                    pairs[j - 1][0] = temp[0];
                    pairs[j - 1][1] = temp[1];
                }
            }
        }
        int min = pairs[0][1];
        int length = 1;
        for (auto it = pairs.begin(); it != pairs.end(); it++) {
            if ((*it)[0] > min) { 
                length++;
                min = (*it)[1];
            }
        }
        return length;
    }
};

int main() {
    Solution solution;
    vector<vector<int>> pairs;
    pairs.push_back(vector<int>({9, 10}));
    pairs.push_back(vector<int>({-4, 9}));
    pairs.push_back(vector<int>({-5, 6}));
    pairs.push_back(vector<int>({-5, 9}));
    pairs.push_back(vector<int>({8, 9}));
    cout << solution.findLongestChain(pairs) << endl;
    return 0;
}