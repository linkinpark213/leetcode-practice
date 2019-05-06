//
// Created by linkinpark213 on 5/6/19.
//

#include <iostream>
#include <vector>

using namespace std;

class Solution {
public:
    int removeElement(vector<int> &nums, int val) {
        if (nums.size() == 0) return 0;
        int count = 0;
        while (count != nums.size()) {
            if (val == nums[count]) {
                nums.erase(nums.begin() + count, nums.begin() + count + 1);
            } else {
                count++;
            }
        }
        return count;
    }
};

int main() {
    Solution solution;
    int array[] = {0, 1, 2, 2, 3, 0, 4, 2};
    vector<int> nums(array, array + sizeof(array) / sizeof(int));
    cout << solution.removeElement(nums, 2);
}