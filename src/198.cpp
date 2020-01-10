#include <iostream>
#include <vector>

using namespace std;

struct Memo {
    int maxRobbed;
    int maxUnrobbed;
    Memo(int a, int b) : maxRobbed(a), maxUnrobbed(b) {};
};

class Solution {
public:
    int robWithMemo(vector<int>& nums, int pos, vector<Memo*> &memos, bool canRob) {
        if (pos == nums.size())
            return 0;
        Memo* record = memos[pos];
        if (record == NULL) {
            int valueRobbed = nums[pos] + robWithMemo(nums, pos + 1, memos, false);
            int valueUnrobbed = robWithMemo(nums, pos + 1, memos, true);
            memos[pos] = new Memo(valueRobbed, valueUnrobbed);
            return canRob ? max(valueRobbed, valueUnrobbed) : valueUnrobbed;
        } else {
            return canRob ? max(record->maxRobbed, record->maxUnrobbed) : record->maxUnrobbed;
        }
    }

    int rob(vector<int>& nums) {
        if (nums.size() == 0) return 0;
        if (nums.size() == 1) return nums[0];
        auto memos = vector<Memo*>(nums.size(), NULL);
        return robWithMemo(nums, 0, memos, true);
    }
};


int main() {
    Solution solution;
    vector<int> nums = {1, 2, 3, 1};
    cout << solution.rob(nums);
    return 0;
}