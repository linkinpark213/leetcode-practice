//
// Created by linkinpark213 on 6/22/19.
//

#include <iostream>
#include <vector>

using namespace std;

class Solution {
public:
    bool validMountainArray(vector<int> &A) {
        if (A.size() < 3) return false;
        bool increasing = true;
        for (int i = 1; i < A.size() - 1; i++) {
            if (increasing) {
                if (A[i] <= A[i - 1]) return false;
                if (A[i] > A[i + 1]) increasing = false;
            } else {
                if (A[i] <= A[i + 1]) return false;
            }
        }
        return !increasing;
    }
};

int main() {
    Solution solution;
    int numbers1[] = {2, 1};
    vector<int> nums1(numbers1, numbers1 + sizeof(numbers1) / sizeof(int));
    cout << solution.validMountainArray(nums1);
    int numbers2[] = {3, 5, 5};
    vector<int> nums2(numbers2, numbers2 + sizeof(numbers2) / sizeof(int));
    cout << solution.validMountainArray(nums2);
    int numbers3[] = {0, 3, 2, 1};
    vector<int> nums3(numbers3, numbers3 + sizeof(numbers3) / sizeof(int));
    cout << solution.validMountainArray(nums3);
}