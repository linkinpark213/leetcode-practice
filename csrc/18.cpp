//
// Created by linkinpark213 on 5/6/19.
//

#include <iostream>
#include <vector>

using namespace std;

class Solution {
    vector<vector<int>> nSum(vector<int> &nums, int target, int n, int l) {
        if (n == 1) {
            for (int i = l; i < nums.size(); i++) {
                if (nums[i] == target) {
                    return vector<vector<int>>(1, vector<int>(1, nums[i]));
                }
            }
            return vector<vector<int>>();
        } else {
            int i = l;
            vector<vector<int>> allAns;
            while (i < nums.size()) {
                vector<vector<int>> ans = nSum(nums, target - nums[i], n - 1, i + 1);
                for (int j = 0; j < ans.size(); j++) {
                    ans[j].insert(ans[j].begin(), nums[i]);
                    allAns.push_back(ans[j]);
                }
                while (i < nums.size() - 1 && nums[i] == nums[i + 1]) i++;
                i++;
            }
            return allAns;
        }
    }

public:
    vector<vector<int>> fourSum(vector<int> &nums, int target) {
        int temp;
        for (int i = 0; i < nums.size(); i++) {
            for (int j = nums.size() - 1; j > i; j--) {
                if (nums[j] < nums[j - 1]) {
                    temp = nums[j];
                    nums[j] = nums[j - 1];
                    nums[j - 1] = temp;
                }
            }
        }
        vector<vector<int>> ans;
        return nSum(nums, target, 4, 0);
    }
};

int main() {
    Solution solution;
    int array[] = {1, 0, -1, 0, -2, 2};
    vector<int> nums(array, array + sizeof(array) / sizeof(int));
    for (vector<int> v : solution.fourSum(nums, 0)) {
        for (int i : v) {
            cout << i << ' ';
        }
        cout << endl;
    }
}