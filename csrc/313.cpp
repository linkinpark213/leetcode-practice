#include <iostream>
#include <vector>

using namespace std;

class Solution {
public:
    int nthSuperUglyNumber(int n, vector<int>& primes) {
        if (n == 1) return 1;
        vector<int> nums = {1};
        int count = 1;
        int minValue = INT_MAX;
        vector<int> ptrs(primes.size(), 0);
        while (count < n) {
            for (int i = 0; i < primes.size(); i++)
                if (primes[i] * nums[ptrs[i]] == nums.back())
                    ptrs[i]++;
            minValue = INT_MAX;
            for (int i = 0; i < primes.size(); i++)
                minValue = min(minValue, primes[i] * nums[ptrs[i]]);
            nums.push_back(minValue);
            count++;
        }
        return nums[n - 1];
    }
};

int main() {
    Solution solution;
    vector<int> primes = {2};
    cout << solution.nthSuperUglyNumber(3, primes);
    return 0;
}