//
// Created by linkinpark213 on 5/6/19.
//
#include <iostream>
#include <vector>

using namespace std;

class Solution {
public:
    vector<int> twoSum(vector<int> &nums, int target) {
        for (int i = 0; i < nums.size(); i++) {
            for (int j = i + 1; j < nums.size(); j++) {
                if (nums[i] + nums[j] == target) {
                    vector<int> ans = vector<int>();
                    ans.push_back(i);
                    ans.push_back(j);
                    return ans;
                }
            }
        }
        return vector<int>(0);
    }
};

int main() {
    Solution solution;
    int nums[] = {2, 7, 11, 15};
    vector<int> vector(nums, nums + sizeof(nums) / sizeof(int));
    for (int i : vector) {
        cout << i << ' ';
    }
}