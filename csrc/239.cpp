//
// Created by linkinpark213 on 5/26/19.
//
#include <iostream>
#include <vector>
#include <deque>

using namespace std;

class Solution {
public:
    vector<int> maxSlidingWindow(vector<int> &nums, int k) {
        if (nums.empty())
            return nums;
        vector<int> ans;
        deque<int> window;
        for (int i = 0; i < k; ++i) {
            while (!window.empty() && nums[window.back()] <= nums[i])
                window.pop_back();
            window.push_back(i);
        }
        ans.push_back(nums[window.front()]);
        for (int i = k; i < nums.size(); ++i) {
            while (!window.empty() && nums[window.back()] <= nums[i])
                window.pop_back();
            while (!window.empty() && window.front() <= i - k)
                window.pop_front();
            window.push_back(i);
            ans.push_back(nums[window.front()]);
        }
        return ans;
    }
};


int main() {
    Solution solution;
    int numbers[] = {9, 10, 9, -7, -4, -8, 2, -6};
    vector<int> nums(numbers, numbers + sizeof(numbers) / sizeof(int));
    vector<int> ans = solution.maxSlidingWindow(nums, 5);
    for (int i : ans)
        cout << i << " ";

}
