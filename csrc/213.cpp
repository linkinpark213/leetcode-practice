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
        if (record ==  NULL) {
            int valueRobbed = nums[pos] + robWithMemo(nums, pos + 1, memos, false);
            int valueUnrobbed = robWithMemo(nums, pos + 1, memos, true);
            memos[pos] = new Memo(valueRobbed, valueUnrobbed);
            return canRob ? max(valueRobbed, valueUnrobbed) : valueUnrobbed;
        } else {
            return canRob? max(record->maxRobbed, record->maxUnrobbed) : record->maxUnrobbed;
        }
    }

    int rob(vector<int>& nums) {
        if (nums.size() == 0) return 0;
        if (nums.size() == 1) return nums[0];
        int temp = nums[nums.size() - 1];
        nums.erase(nums.begin() + nums.size() - 1);
        auto memos = vector<Memo*>(nums.size(), NULL);
        int ans1 = robWithMemo(nums, 0, memos, true);
        nums.push_back(temp);
        nums.erase(nums.begin());
        memos = vector<Memo*>(nums.size(), NULL);
        int ans2 = robWithMemo(nums, 0, memos, true);
        return max(ans1, ans2);
    }
};


int main() {
    Solution solution;
    vector<int> nums = {1, 2};
    cout << solution.rob(nums);
    return 0;
}