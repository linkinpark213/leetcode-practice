//
// Created by linkinpark213 on 5/29/19.
//
#include <iostream>
#include <vector>

using namespace std;

class Solution {
public:
    vector<int> intersect(vector<int> &nums1, vector<int> &nums2) {
        vector<int> ans;
        for (int i:nums1) {
            for (int j = 0; j < nums2.size(); j++) {
                if (i == nums2[j]) {
                    ans.push_back(nums2[j]);
                    nums2.erase(nums2.begin() + j);
                    break;
                }
            }
        }
        return ans;
    }
};

int main() {
    Solution solution;
    int numbers1[] = {4, 9, 5};
    int numbers2[] = {9, 4, 9, 8, 4};
    vector<int> nums1(numbers1, numbers1 + sizeof(numbers1) / sizeof(int));
    vector<int> nums2(numbers2, numbers2 + sizeof(numbers2) / sizeof(int));
    vector<int> ans = solution.intersect(nums1, nums2);
    for (int i : ans)
        cout << i << " ";
    cout << endl;
}