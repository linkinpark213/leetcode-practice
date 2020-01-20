#include <iostream>
#include <vector>

using namespace std;

class Solution {
public:
    int nthUglyNumber(int n) {
        if (n <= 5) return n;
        vector<int> nums = {1, 2, 3, 4, 5};
        int count = 5;
        int ptr2 = 2, ptr3 = 1, ptr5 = 1;
        while (count < n) {
            if (nums[ptr2] * 2 == nums.back()) ptr2++;
            if (nums[ptr3] * 3 == nums.back()) ptr3++;
            if (nums[ptr5] * 5 == nums.back()) ptr5++;
            nums.push_back(min(min(nums[ptr2] * 2, nums[ptr3] * 3), nums[ptr5] * 5));
            count++;
        }
        return nums[n - 1];
    }
};

int main() {
    Solution solution;
    cout << solution.nthUglyNumber(10);
    return 0;
}