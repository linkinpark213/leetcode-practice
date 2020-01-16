#include <iostream>
#include <vector>

using namespace std;

class Solution {
    int lengthOfLISUntil(vector<int> &nums, int pos, int* memo) { 
        int maxLength = 1;
        for (int i = 0; i < pos; i++) {
            if (nums[pos] > nums[i]) {
                maxLength = max(maxLength, 1 + memo[i]);
            }
        }
        memo[pos] = maxLength;
        return maxLength;
    }

   public:
    int lengthOfLIS(vector<int> &nums) {
        if (nums.size() < 2) return nums.size();
        int memo[nums.size()];
        int maxLength = 0;
        for (int i = 0; i < nums.size(); i++) memo[i] = 0;
        for (int i = 0; i < nums.size(); i++) maxLength = max(lengthOfLISUntil(nums, i, memo), maxLength);
        return maxLength;
    }
};

int main() {
    Solution solution;
    vector<int> nums = {10, 9, 2, 5, 3, 7, 101, 18};
    cout << solution.lengthOfLIS(nums);
    return 0;
}