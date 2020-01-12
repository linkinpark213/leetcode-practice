#include <iostream>
#include <vector>
#include <set>

using namespace std;

class Solution {
public:
    int longestConsecutive(vector<int>& nums) {
        if (nums.size() == 0) return 0;
        set<int> numsSet;
        int maxStreak = 1, count = 1;
        for (int i = 0; i < nums.size(); i++) {
            numsSet.insert(nums[i]);
        }
        for (auto it = numsSet.begin(); it != numsSet.end(); it++) {
            count = 1;
            while (true) {
                if (it != numsSet.end() && numsSet.find(*it + 1) != numsSet.end()) {
                    it++;
                    count++;
                } else break;
            }
            maxStreak = max(maxStreak, count);
        }
        return maxStreak;
    }
};

int main() {
    Solution solution;
    vector<int> nums = {100, 4, 200, 1, 3, 2};
    cout << solution.longestConsecutive(nums);
    return 0;
}