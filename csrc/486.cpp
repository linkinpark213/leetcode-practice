#include <iostream>
#include <vector>

using namespace std;

class Solution {
    bool CanWin(vector<int>& nums, int begin, int end, int reward, int myTurn) {
        if (begin == end) return reward + myTurn * nums[begin] >= 0;
        if (myTurn == 1) 
            return CanWin(nums, begin + 1, end, reward + nums[begin], -1) || CanWin(nums, begin, end - 1, reward + nums[end], -1);
        else
            return CanWin(nums, begin + 1, end, reward - nums[begin], 1) && CanWin(nums, begin, end - 1, reward - nums[end], 1);
    }

   public:
    bool PredictTheWinner(vector<int>& nums) {
        return CanWin(nums, 0, nums.size() - 1, 0, 1);
    }
};

int main() {
    Solution solution;
    vector<int> nums1 = {1,1,1};
    cout << solution.PredictTheWinner(nums1);
    vector<int> nums2 = {1,5,2};
    cout << solution.PredictTheWinner(nums2);
    vector<int> nums3 = {2,4,55,6,8};
    cout << solution.PredictTheWinner(nums3);
    return 0;
}