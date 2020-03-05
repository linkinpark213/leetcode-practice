//
// Created by linkinpark213 on 6/22/19.
//

#include <iostream>
#include <vector>
#include <stack>

using namespace std;

class Solution {
public:
    vector<vector<int>> permute(vector<int> &nums) {
        vector<vector<int>> ans;
        if (nums.size() > 1) {
            for (int i = 0; i < nums.size(); i++) {
                int n = nums[i];
                nums.erase(nums.begin() + i);
                vector<vector<int>> prev_ans = permute(nums);
                for (vector<int> v : prev_ans) {
                    v.insert(v.begin(), n);
                    ans.push_back(v);
                }
                nums.insert(nums.begin() + i, n);
            }
        } else {
            ans.emplace_back(vector<int>(1, nums[0]));
        }
        return ans;
    }
};

int main() {
    Solution solution;
    int numbers[] = {1, 2, 3};
    vector<int> nums(numbers, numbers + sizeof(numbers) / sizeof(int));
    for (const vector<int> &v: solution.permute(nums)) {
        for (int i: v)
            cout << i << ' ';
        cout << endl;
    }
}