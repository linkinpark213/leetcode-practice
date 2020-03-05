//
// Created by linkinpark213 on 5/22/19.
//

#include <iostream>
#include <vector>
#include <climits>

using namespace std;

class Solution {
public:
    int findPeakElement(vector<int> &nums) {
        nums.insert(nums.begin(), INT_MIN);
        nums.push_back(INT_MIN);
        int l = 1, r = nums.size() - 2;
        while (l < r) {
            int middle = (l + r) / 2;
            if (nums[middle] > nums[middle - 1] && nums[middle] > nums[middle + 1]) {
                return middle - 1;
            } else if (nums[middle] < nums[middle - 1]) {
                r = middle - 1;
            } else {
                l = middle + 1;
            }
        }
        return l - 1;
    }
};

int main() {
    Solution solution;
    auto *nums = new vector<int>();
    nums->push_back(1);
    nums->push_back(2);
    nums->push_back(3);
    nums->push_back(1);
    cout << solution.findPeakElement(*nums);
    cout << endl;

    nums = new vector<int>();
    nums->push_back(1);
    nums->push_back(2);
    nums->push_back(1);
    nums->push_back(3);
    nums->push_back(5);
    nums->push_back(6);
    nums->push_back(4);
    cout << solution.findPeakElement(*nums);
    cout << endl;

    nums = new vector<int>();
    nums->push_back(2);
    nums->push_back(1);
    cout << solution.findPeakElement(*nums);
    cout << endl;

    nums = new vector<int>();
    nums->push_back(3);
    nums->push_back(2);
    nums->push_back(1);
    cout << solution.findPeakElement(*nums);
    cout << endl;
}