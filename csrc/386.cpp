#include <iostream>
#include <vector>

using namespace std;

class Solution {
    void insertByPrefix(int n, int prefix, vector<int>& nums) {
        for (int i = 0; i < 10; i++) {
            if (prefix * 10 + i > n) return;
            nums.push_back(prefix * 10 + i);
            if ((prefix * 10 + i) * 10 <= n) {
                insertByPrefix(n, prefix * 10 + i, nums);
            }
        }
    }
public:
    vector<int> lexicalOrder(int n) {
        vector<int> ans;
        for (int i = 1; i < 10; i++) {
            if (i <= n) { 
                ans.push_back(i);
                insertByPrefix(n, i, ans);
            } else break;
        }
        return ans;
    }
};

int main() {
    Solution solution;
    auto ans = solution.lexicalOrder(13);
    for (auto it = ans.begin(); it != ans.end(); it++)
        cout << *it << " ";
    return 0;
}