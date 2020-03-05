//
// Created by linkinpark213 on 6/22/19.
//

#include <iostream>
#include <vector>

using namespace std;

class Solution {
public:
    bool canPartition(vector<int> &nums) {
        int sum = 0;
        for (int i : nums) sum += i;
        if (sum % 2 == 1) return false;
        int target = sum / 2;
        for (int i : nums)
            if (i > target) return false;
        vector<bool> dp(target + 1, false);
        dp[0] = true;
        for (int i : nums)
            for (int j = target; j >= i; j--)
                dp[j] = dp[j - i] || dp[j];
        return dp[target];
    }
};

int main() {
    Solution solution;
    int numbers1[] = {1, 5, 11, 5};
    vector<int> nums1(numbers1, numbers1 + sizeof(numbers1) / sizeof(int));
    cout << solution.canPartition(nums1) << endl;
    int numbers2[] = {1, 2, 3, 5};
    vector<int> nums2(numbers2, numbers2 + sizeof(numbers2) / sizeof(int));
    cout << solution.canPartition(nums2) << endl;
    int numbers3[] = {100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100,
                      100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100,
                      100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100,
                      100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100,
                      100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100,
                      100, 100, 100, 100, 100};
    vector<int> nums3(numbers3, numbers3 + sizeof(numbers3) / sizeof(int));
    cout << solution.canPartition(nums3) << endl;
    int numbers4[] = {1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1,
                      1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1,
                      1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1,
                      100};
    vector<int> nums4(numbers4, numbers4 + sizeof(numbers4) / sizeof(int));
    cout << solution.canPartition(nums4) << endl;
    int numbers5[] = {1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1,
                      1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1,
                      1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1,
                      97, 95};
    vector<int> nums5(numbers5, numbers5 + sizeof(numbers5) / sizeof(int));
    cout << solution.canPartition(nums5) << endl;
    int numbers6[] = {2, 2, 3, 5};
    vector<int> nums6(numbers6, numbers6 + sizeof(numbers6) / sizeof(int));
    cout << solution.canPartition(nums6) << endl;

}