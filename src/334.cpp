#include <iostream>
#include <vector>

using namespace std;

class Solution {
public:
    bool increasingTriplet(vector<int>& nums) {
        if (nums.size() < 3) return false;
        int minValue = INT_MAX;
        int secondValue = INT_MAX;
        for (int i = 0; i < nums.size(); i++) {
            if (minValue >= nums[i]) minValue = nums[i];
            else if (secondValue >= nums[i]) secondValue = nums[i];
            else return true;
        }
        return false;
    }
};

int main() {
    Solution solution;
    vector<int> nums = {1, 2, 3, 4, 5};
    cout << solution.increasingTriplet(nums);
    return 0;
}