//
// Created by linkinpark213 on 5/6/19.
//

#include <iostream>
#include <vector>

#define INT_MAX 2147483647
#define INT_MIN (-INT_MAX - 1)
using namespace std;

class Solution {
public:
    int threeSumClosest(vector<int> &nums, int target) {
        int min_distance = INT_MAX;
        int distance = 0, best_sum = 0, sum = 0;
        for (int i = 0; i < nums.size() - 2; i++) {
            for (int j = i + 1; j < nums.size() - 1; j++) {
                for (int k = j + 1; k < nums.size(); k++) {
                    sum = nums[i] + nums[j] + nums[k];
                    distance = sum - target;
                    if (distance < 0)
                        distance = -distance;
                    if (distance < min_distance) {
                        best_sum = sum;
                        min_distance = distance;
                    }
                }
            }
        }
        return best_sum;
    }
};

int main() {
    Solution solution;
    int array[] = {-1, 2, 1, -4};
    vector<int> nums(array, array + sizeof(array) / sizeof(int));
    cout << solution.threeSumClosest(nums, 1);
}