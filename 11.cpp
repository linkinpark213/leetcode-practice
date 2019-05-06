//
// Created by linkinpark213 on 5/6/19.
//

#include <iostream>
#include <vector>

using namespace std;

class Solution {
public:
    int maxArea(vector<int> &height) {
        int max_volume = 0;
        int volume;
        for (int i = 0; i < height.size(); i++) {
            if (height[i] > 0)
                for (int j = i + (max_volume / height[i]); j < height.size(); j++) {
                    volume = (j - i) * min(height[i], height[j]);
                    if (volume > max_volume) {
                        max_volume = volume;
                    }
                }
        }
        return max_volume;
    }
};

int main() {
    Solution solution;
    int nums[] = {1, 8, 6, 2, 5, 4, 8, 3, 7};
    vector<int> height(nums, nums + sizeof(nums) / sizeof(int));
    cout << solution.maxArea(height);
}