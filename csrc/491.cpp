#include <iostream>
#include <vector>
#include <unordered_set>

using namespace std;

class Solution {
    void findRecursively(vector<int>& nums, vector<vector<int>>& subsequences, vector<int> subsequence, int pos, int length, int max) {
        if (length > 1) subsequences.push_back(subsequence);

        unordered_set<int> usedNumbers;
        for (int i = pos; i < nums.size(); i++) {
            if (nums[i] < max || usedNumbers.find(nums[i]) != usedNumbers.end()) continue;
            usedNumbers.insert(nums[i]);

            subsequence.push_back(nums[i]);
            findRecursively(nums, subsequences, subsequence, i + 1, length + 1, nums[i]);
            subsequence.pop_back();
        }
    }

public:
    vector<vector<int>> findSubsequences(vector<int>& nums) {
        vector<vector<int>> subsequences;
        findRecursively(nums, subsequences, vector<int>(), 0, 0, INT_MIN);
        return subsequences;
    }
};

int main() {
    Solution solution;
    vector<int> nums = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15};
    auto ans = solution.findSubsequences(nums);
    for (auto it = ans.begin(); it != ans.end(); it++) {
        for (auto it1 = it->begin(); it1 != it->end(); it1++) {
            cout << *it1 << " ";
        }
        cout << endl;
    }
    return 0;
}