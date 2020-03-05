#include <iostream>
#include <unordered_map>
#include <vector>

using namespace std;

static const int states[] = {1, 7, 49, 343, 2401, 16807};

class Solution {
    int vector2Int(vector<int>& special, int withPrice) {
        int needsState = 0;
        for (int i = 0; i < special.size() - withPrice; i++)
            needsState += states[i] * special[i];
        return needsState;
    }

    int canBuy(int special, int target) {
        int temp1 = special, temp2 = target;
        for (int i = 0; i < 6; i++) {
            if ((target % 7) < (special % 7)) return false;
            target = target / 7;
            special = special / 7;
        }
        cout << "Can buy " << temp1 << " to " << temp2 - temp1 << " when target is " << temp2 << endl;
        return true;
    }

    int shoppingHelper(int needs, unordered_map<int, int>& specials,
                       unordered_map<int, int>& memo) {
        if (needs == 0) return 0;
        if (memo.find(needs) != memo.end()) return memo.find(needs)->second;
        int minCost = INT_MAX;
        for (auto it = specials.begin(); it != specials.end(); it++) {
            if (canBuy(it->first, needs)) {
                int cashSpent = it->second + shoppingHelper(needs - it->first,
                                                            specials, memo);
                if (minCost > cashSpent) minCost = cashSpent;
            }
        }
        memo.insert(pair<int, int>(needs, minCost));
        return minCost;
    }

   public:
    int shoppingOffers(vector<int>& price, vector<vector<int>>& special,
                       vector<int>& needs) {
        unordered_map<int, int> memo;
        unordered_map<int, int> specialInts;
        int target = vector2Int(needs, 0);
        for (int i = 0; i < price.size(); i++)
            specialInts[states[i]] = price[i];
        for (auto it = special.begin(); it != special.end(); it++) {
            int state = vector2Int(*it, 1);
            int price = (*it)[it->size() - 1];
            if (specialInts.find(state) != specialInts.end())
                price = min(price, specialInts[state]);
            specialInts[state] = price;
        }
        int minCost = shoppingHelper(target, specialInts, memo);
        // for (auto it = memo.begin(); it != memo.end(); it++) {
            // cout << it->first << " " << it->second << endl;
        // }
        return minCost;
    }
};

int main() {
    Solution solution;
    vector<int> price = {6, 7, 7, 6, 8, 4};
    vector<vector<int>> special = {
        {0, 0, 0, 1, 0, 0, 6},  {1, 1, 1, 5, 2, 3, 21}, {6, 5, 5, 4, 5, 6, 34},
        {2, 6, 1, 4, 2, 6, 37}, {2, 2, 6, 1, 2, 4, 18}, {0, 2, 3, 2, 3, 5, 15}};
    vector<int> needs = {3, 1, 1, 0, 4, 5};
    cout << solution.shoppingOffers(price, special, needs);
    return 0;
}