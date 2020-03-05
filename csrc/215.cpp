//
// Created by linkinpark213 on 5/29/19.
//

#include <iostream>
#include <vector>
#include <climits>

using namespace std;

class Solution {
public:
    int findKthLargest(vector<int> &nums, int k) {
        int max = INT_MIN;
        int pos = -1;
        for (int i = 0; i < k; i++) {
            max = INT_MIN;
            for (int j = 0; j < nums.size(); j++) {
                if (nums[j] > max) {
                    max = nums[j];
                    pos = j;
                }
            }
            if (i < k - 1)
                nums.erase(nums.begin() + pos);
            else
                return nums[pos];
        }
        return nums[0];
    }
};

int main() {
    Solution solution;
    int numbers[] = {3, 2, 3, 1, 2, 4, 5, 5, 6};
    vector<int> nums(numbers, numbers + sizeof(numbers) / sizeof(int));
    cout << solution.findKthLargest(nums, 4);
}