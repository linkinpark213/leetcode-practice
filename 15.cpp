//
// Created by linkinpark213 on 5/6/19.
//

#include <iostream>
#include <vector>

using namespace std;

class Solution {
public:
    vector<vector<int>> threeSum(vector<int> &nums) {
        vector<vector<int>> ans;
        if (nums.size() < 3) return ans;
        for (int i = 0; i < nums.size(); i++) {
            for (int j = nums.size() - 1; j > i; j--) {
                if (nums[j] < nums[j - 1]) {
                    int temp = nums[j];
                    nums[j] = nums[j - 1];
                    nums[j - 1] = temp;
                }
            }
        }
        for (int i = 0; i < nums.size() - 2; i++) {
            if (i == 0 || nums[i] != nums[i - 1]) {
                int lp = i + 1, rp = nums.size() - 1;
                while (lp < rp) {
                    int sum = nums[lp] + nums[rp] + nums[i];
                    if (sum == 0) {
                        vector<int> row;
                        row.push_back(nums[i]);
                        row.push_back(nums[lp]);
                        row.push_back(nums[rp]);
                        ans.push_back(row);
                        while (lp < rp && nums[lp + 1] == nums[lp]) lp++;
                        while (rp > lp && nums[rp - 1] == nums[rp]) rp--;
                        lp++;
                        rp--;
                    } else if (sum < 0) {
                        lp++;
                    } else if (sum > 0) {
                        rp--;
                    }
                }
            }
        }
        return ans;
    }
};

int main() {
    Solution solution;
    int array[] = {-1, 0, 1, 2, -1, -4};
    vector<int> nums(array, array + sizeof(array) / sizeof(int));
    for (vector<int> v : solution.threeSum(nums)) {
        for (int i : v) {
            cout << i << ' ';
        }
        cout << endl;
    }
}