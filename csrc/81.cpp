//
// Created by linkinpark213 on 7/2/19.
//

#include <iostream>
#include <vector>

using namespace std;

class Solution {
public:
    bool search(vector<int> &nums, int target) {
        if (nums.empty())
            return false;
        if (nums[0] == target || nums[nums.size() - 1] == target)
            return true;
        bool left = (nums[0] < target);
        if (left) {
            for (int i = 1; i < nums.size(); i++) {
                if (nums[i] == target) return true;
                else if (nums[i] > target) return false;
                else if (nums[i] < nums[i - 1]) return false;
            }
        } else {
            for (int i = nums.size() - 2; i >= 0; i--) {
                if (nums[i] == target) return true;
                else if (nums[i] < target) return false;
                else if (nums[i] > nums[i + 1]) return false;
            }
        }
        return false;
    }
};

int main() {
    Solution solution;
    int numbers1[] = {2, 5, 6, 0, 0, 1, 2};
    vector<int> nums1(numbers1, numbers1 + sizeof(numbers1) / sizeof(int));
    cout << solution.search(nums1, 0);
    int numbers2[] = {2, 5, 6, 0, 0, 1, 2};
    vector<int> nums2(numbers2, numbers2 + sizeof(numbers2) / sizeof(int));
    cout << solution.search(nums2, 3);
}