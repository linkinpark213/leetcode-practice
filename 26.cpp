//
// Created by linkinpark213 on 5/6/19.
//

#include <iostream>
#include <vector>

using namespace std;

class Solution {
public:
    int removeDuplicates(vector<int> &nums) {
        if (nums.size() == 0) return 0;
        if (nums.size() == 1) return 1;
        int value = nums[0];
        int count = 1;
        int i = 1;
        while (count < nums.size()) {
            if (nums[count] != value) {
                value = nums[count];
                count++;
            } else {
                nums.erase(nums.begin() + count, nums.begin() + count + 1);
            }
        }
        return count;
    }
};

int main() {
    Solution solution;
    int array[] = {0, 0, 1, 1, 1, 2, 2, 3, 3, 4};
    vector<int> nums(array, array + sizeof(array) / sizeof(int));
    cout << solution.removeDuplicates(nums);
}
