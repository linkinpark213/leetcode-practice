//
// Created by linkinpark213 on 6/8/19.
//
#include <iostream>
#include <vector>

using namespace std;

class Solution {
public:
    vector<vector<int>> transpose(vector<vector<int>> &A) {
        vector<vector<int>> A_T;
        for (int i = 0; i < A[0].size(); i++) {
            vector<int> row;
            for (int j = 0; j < A.size(); j++) {
                row.push_back(A[j][i]);
            }
            A_T.push_back(row);
        }
        return A_T;
    }
};

int main() {
    Solution solution;
    int nums1[] = {1, 2, 3};
    int nums2[] = {4, 5, 6};
    vector<int> row1(nums1, nums1 + sizeof(nums1) / sizeof(int));
    vector<int> row2(nums2, nums2 + sizeof(nums2) / sizeof(int));
    vector<vector<int>> A;
    A.push_back(row1);
    A.push_back(row2);
    vector<vector<int>> A_T = solution.transpose(A);
    for (vector<int> row : A_T) {
        for (int i : row) {
            cout << i << " ";
        }
        cout << endl;
    }
}